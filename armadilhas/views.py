from django.shortcuts import render, get_object_or_404
from inicio.models import Propriedade

def armadilhas(request, propriedade_id):
    propriedade = get_object_or_404(Propriedade, id=propriedade_id)
    armadilhas = propriedade.armadilhas.all()
    return render(request, 'armadilhas/armadilhas.html', {'propriedade': propriedade, 'armadilhas': armadilhas})
