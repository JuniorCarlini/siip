from django import forms
from inicio.models import Armadilha

class ArmadilhaForm(forms.ModelForm):
    class Meta:
        model = Armadilha
        fields = ['identificador', 'coordenadas_geograficas']