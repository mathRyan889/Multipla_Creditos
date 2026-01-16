from django import forms
from .models import RegisterLead

class RegisterLeadForm(forms.ModelForm):
    class Meta:
        model = RegisterLead
        fields = ['name', 'whatsapp', 'cpf', 'services']
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Seu nome',
                'class': 'input'
            }),
            'whatsapp': forms.TextInput(attrs={
                'placeholder': 'Seu WhatsApp',
                'class': 'input'
            }),
            'cpf': forms.TextInput(attrs={
                'placeholder': 'Seu CPF',
                'class': 'input'
            }),
            'services': forms.Select(attrs={
                'class': 'select'
            }),
        }