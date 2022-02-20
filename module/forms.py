from django.core import validators
from django import forms
from .models import Module

class ModuleRegistration(forms.ModelForm):
    class Meta: 
     model = Module
     fields = ['title', 'coeff','specialite']
     widgets = {
        'title': forms.TextInput(attrs={'class': 'form-control'}),
        'coeff': forms.NumberInput(attrs={'class': 'form-control'}),
         'specialite.titre': forms.TextInput(attrs={'class': 'form-control'}),
     }