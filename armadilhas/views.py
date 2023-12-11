# armadilhas/views.py
from django.shortcuts import render, get_object_or_404
from inicio.models import Propriedade, Armadilha
from armadilhas.forms import ArmadilhaForm

def armadilhas(request, propriedade_id):
    propriedade = get_object_or_404(Propriedade, id=propriedade_id)
    armadilhas = propriedade.armadilhas.all()
    return render(request, 'armadilhas/armadilhas.html', {'propriedade': propriedade, 'armadilhas': armadilhas})
