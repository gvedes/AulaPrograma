from django import forms
from django.forms import ModelForm
from .models import Produtos

class ProdutoForm(ModelForm):
    class Meta:
        model = Produtos
        fields = ['produto', 'cor', 'descricao']
        widgets = {
            'produto': forms.TextInput(attrs={'class': 'input'}),
            'cor': forms.TextInput(attrs={'class': 'input'}),
            'descricao': forms.Textarea(attrs={'class': 'textarea'}),
        }