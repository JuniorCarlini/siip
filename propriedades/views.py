from django.shortcuts import render, get_object_or_404, redirect
from inicio.models import Proprietario, Propriedade
from propriedades.forms import PropriedadeForm  # Certifique-se de importar o seu formulário

def propriedades(request, proprietario_id):
    # Recupere o proprietário com base no ID fornecido ou retorne um erro 404 se não existir
    proprietario = get_object_or_404(Proprietario, id=proprietario_id)

    # Recupere as propriedades associadas a esse proprietário
    propriedades = Propriedade.objects.filter(proprietario=proprietario)

    # Se o formulário de criação de propriedade for submetido
    if request.method == 'POST':
        form = PropriedadeForm(request.POST)
        if form.is_valid():
            propriedade = form.save(commit=False)
            propriedade.proprietario = proprietario
            propriedade.save()
            # Redirecione para a mesma página para evitar o envio de dados novamente ao atualizar a página
            return redirect('propriedades', proprietario_id=proprietario_id)
    else:
        form = PropriedadeForm()

    # Passe o proprietário, suas propriedades e o formulário para o contexto do template
    context = {'proprietario': proprietario, 'propriedades': propriedades, 'form': form}

    return render(request, 'propriedades/propriedades.html', context)
