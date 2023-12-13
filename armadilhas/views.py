from django.shortcuts import render, get_object_or_404, redirect
from inicio.models import Propriedade, Armadilha
from armadilhas.forms import ArmadilhaForm  # Corrigir o nome do formulário

def armadilhas(request, propriedade_id):
    propriedade = get_object_or_404(Propriedade, id=propriedade_id)

    armadilhas = propriedade.armadilhas.all()

    # Se o formulário de criação de armadilha for submetido
    if request.method == 'POST':
        form = ArmadilhaForm(request.POST)  # Corrigir o nome do formulário
        if form.is_valid():
            armadilha = form.save(commit=False)
            armadilha.propriedade = propriedade
            armadilha.save()

            return redirect('armadilhas', propriedade_id=propriedade_id)
    else:
        form = ArmadilhaForm()  # Corrigir o nome do formulário

    context = {'propriedade': propriedade, 'armadilhas': armadilhas, 'form': form}  # Corrigir o nome da variável

    return render(request, 'armadilhas/armadilhas.html', context)
