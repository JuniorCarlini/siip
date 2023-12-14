from django.shortcuts import render, get_object_or_404, redirect
from inicio.models import Propriedade, Armadilha
from armadilhas.forms import ArmadilhaForm 

def armadilhas(request, propriedade_id):
    propriedade = get_object_or_404(Propriedade, id=propriedade_id)

    armadilhas = propriedade.armadilhas.all()

    if request.method == 'POST':
        form = ArmadilhaForm(request.POST) 
        if form.is_valid():
            armadilha = form.save(commit=False)
            armadilha.propriedade = propriedade
            armadilha.save()

            return redirect('armadilhas', propriedade_id=propriedade_id)
    else:
        form = ArmadilhaForm() 

    context = {'propriedade': propriedade, 'armadilhas': armadilhas, 'form': form}  # Corrigir o nome da variável

    return render(request, 'armadilhas/armadilhas.html', context)
