from django.shortcuts import render, get_object_or_404, redirect
from inicio.models import Proprietario, Propriedade
from propriedades.forms import PropriedadeForm

def propriedades(request, proprietario_id):
    proprietario = get_object_or_404(Proprietario, id=proprietario_id) 
    propriedades = Propriedade.objects.filter(proprietario=proprietario) 

    if request.method == 'POST':
        form = PropriedadeForm(request.POST)
        if form.is_valid():
            propriedade = form.save(commit=False)
            propriedade.proprietario = proprietario
            propriedade.save()
            
            return redirect('propriedades', proprietario_id=proprietario_id) 
    else:
        form = PropriedadeForm()

    context = {'proprietario': proprietario, 'propriedades': propriedades, 'form': form}
    return render(request, 'propriedades/propriedades.html', context)
