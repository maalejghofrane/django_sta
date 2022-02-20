from django.core import validators
from django import forms
from .models import Matiere

class MatiereRegistration(forms.ModelForm):
    CHOICES = [(1, 'Oui'), (2, 'Non')]
    ds = forms.ChoiceField(choices=CHOICES)
    exam = forms.ChoiceField(choices=CHOICES)
    tp = forms.ChoiceField(choices=CHOICES)

    class Meta: 
     model = Matiere
     fields = ['titre','ds','exam','tp','coeff','module']
     widgets = {
        'titre': forms.TextInput(attrs={'class': 'form-control'}),
         'ds': forms.TextInput(attrs={'class': 'form-control'}),
         'exam': forms.TextInput(attrs={'class': 'form-control'}),
         'tp': forms.TextInput(attrs={'class': 'form-control'}),
         'coeff': forms.NumberInput(attrs={'class': 'form-control'}),
         'module.title': forms.TextInput(attrs={'class': 'form-control'}),
     }


     