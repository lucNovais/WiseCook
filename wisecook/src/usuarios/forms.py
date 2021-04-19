from django import forms
from .models import Usuario

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = [
            'nome',
            'restricoes',
        ]

class UsuarioFormComplete(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = [
            'idusuario',
            'nome',
            'restricoes',
        ]