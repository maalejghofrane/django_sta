from django.core import validators
from django import forms
from .models import Specialite

class SpecialiteRegistration(forms.ModelForm):
    class Meta: 
     model = Specialite
     fields = ['titre', 'niveau']
     widgets = {
        'titre': forms.TextInput(attrs={'class': 'form-control'}),
        'coeff': forms.NumberInput(attrs={'class': 'form-control'}),
     }