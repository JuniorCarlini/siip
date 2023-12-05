from django.shortcuts import render, get_object_or_404
from inicio.models import Proprietario, Propriedade

def propriedades(request, proprietario_id):
    # Recupere o proprietário com base no ID fornecido ou retorne um erro 404 se não existir
    proprietario = get_object_or_404(Proprietario, id=proprietario_id)
    
    # Recupere as propriedades associadas a esse proprietário
    propriedades = Propriedade.objects.filter(proprietario=proprietario)
    
    # Passe o proprietário e suas propriedades para o contexto do template
    context = {'proprietario': proprietario, 'propriedades': propriedades}
    
    return render(request, 'propriedades/propriedades.html', context)
