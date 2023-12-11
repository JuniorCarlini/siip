from django.shortcuts import render, get_object_or_404, redirect
from inicio.models import Proprietario, Propriedade
from propriedades.forms import PropriedadeForm

def propriedades(request, proprietario_id):
    proprietario = get_object_or_404(Proprietario, id=proprietario_id) # Recupere o proprietário com base no ID fornecido ou retorne um erro 404 se não existir

    propriedades = Propriedade.objects.filter(proprietario=proprietario) # Recupere as propriedades associadas a esse proprietário

    # Se o formulário de criação de propriedade for submetido
    if request.method == 'POST':
        form = PropriedadeForm(request.POST)
        if form.is_valid():
            propriedade = form.save(commit=False)
            propriedade.proprietario = proprietario
            propriedade.save()
            
            return redirect('propriedades', proprietario_id=proprietario_id) # Redireciona para a mesma página para evitar o envio de dados novamente ao atualizar a página
    else:
        form = PropriedadeForm()

    context = {'proprietario': proprietario, 'propriedades': propriedades, 'form': form}# Passa o proprietário, suas propriedades e o formulário para o contexto do template

    return render(request, 'propriedades/propriedades.html', context)
