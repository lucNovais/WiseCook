from django import forms
from .models import Possui

class PossuiForm(forms.ModelForm):
    class Meta:
        model = Possui
        fields = [
            'nomealimento',
            'datavalidade',
            'quantidade',
        ]

class UserPossuiForm(forms.ModelForm):
    class Meta:
        model = Possui
        fields = [
            'idusuario',
            'nomealimento',
            'datavalidade',
            'quantidade',
        ]