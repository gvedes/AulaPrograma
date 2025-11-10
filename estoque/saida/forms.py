from django import forms
from django.forms import ModelForm
from .models import Saidas

class SaidaForm(ModelForm):
    class Meta:
        model = Saidas
        fields = ['produto', 'quantidade', 'preco']
        widgets = {
            'produto': forms.Select(attrs={'class': 'input'}),
            'quantidade': forms.NumberInput(attrs={'class': 'input'}),
            'preco': forms.NumberInput(attrs={'class': 'input'}),
        }