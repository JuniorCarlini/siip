# views.py no seu novo app
from django.shortcuts import render
from inicio.models import Propriedade

def propriedades(request, proprietario_id):
    
    # Recupere as propriedades do proprietário do banco de dados
    propriedades = Propriedade.objects.filter(proprietario_id=proprietario_id)
    
    # Passe as propriedades para o contexto do template
    context = {'proprietario_id': proprietario_id, 'propriedades': propriedades}
    
    return render(request, 'propriedades/propriedades.html', {'proprietario_id': 1})

