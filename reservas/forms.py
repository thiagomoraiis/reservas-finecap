from django import forms
from .models import Stands, Reserva


class StandsModelForm(forms.ModelForm):
    class Meta:
        model = Stands
        fields = '__all__'

    widgets = {
        'localizacao': forms.TextInput(attrs={'class': 'form-control'}),
        'valor': forms.NumberInput(attrs={'class': 'form-control'})
    }


class ReservaModelForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = '__all__'

    widgets = {
        'stand': forms.Select(attrs={'class': 'form-control'}),
        'nome_empresa': forms.TextInput(attrs={'class': 'form-control'}),
        'categoria_empresa': forms.Select(attrs={'class': 'form-control'}),
        'cnpj': forms.TextInput(attrs={'class': 'form-control'}),
        'quitado': forms.RadioSelect(attrs={'class': 'form-control'}),
    }
