from django import forms
from .models import Proprietario

class ProprietarioForm(forms.ModelForm):
    class Meta:
        model = Proprietario
        fields = ['nome', 'imagem', 'numero_telefone', 'email']