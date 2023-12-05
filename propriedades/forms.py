from django import forms
from inicio.models import Propriedade

class PropriedadeForm(forms.ModelForm):
    class Meta:
        model = Propriedade
        fields = ['nome_propriedade', 'endereco']