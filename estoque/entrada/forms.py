from django import forms
from django.forms import ModelForm
from .models import Entradas

class EntradaForm(ModelForm):
    class Meta:
        model = Entradas
        fields = ['produto', 'quantidade', 'preco']
        widgets = {
            'produto': forms.Select(attrs={'class': 'input'}),
            'quantidade': forms.NumberInput(attrs={'class': 'input'}),
            'preco': forms.NumberInput(attrs={'class': 'input'}),
        }