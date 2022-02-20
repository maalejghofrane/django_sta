from django.core import validators
from django import forms
from .models import Note

class NoteRegistration(forms.ModelForm):
    class Meta: 
     model = Note
     fields = ['user', 'matiere','note_ds','note_tp','note_exam']
     widgets = {
        'user.name': forms.TextInput(attrs={'class': 'form-control'}),
        'matiere.titre': forms.NumberInput(attrs={'class': 'form-control'}),
         'note_ds': forms.TextInput(attrs={'class': 'form-control'}),
         'note_tp': forms.TextInput(attrs={'class': 'form-control'}),
         'note_exam': forms.TextInput(attrs={'class': 'form-control'}),
     }