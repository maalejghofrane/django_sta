from django.core import validators
from django import forms
from .models import User

class StudentRegistration(forms.ModelForm):
    class Meta: 
     model = User
     fields = ['name', 'email','age','tel','niveau','password','specialite']
   #   choices = [('1', 'First'), ('2', 'Second'), ('3','third')]
     widgets = {
        'name': forms.TextInput(attrs={'class': 'form-control'}),
        'email': forms.EmailInput(attrs={'class': 'form-control'}),
         'age': forms.NumberInput(attrs={'class': 'form-control'}),
         'tel': forms.NumberInput(attrs={'class': 'form-control'}),
        'niveau': forms.NumberInput(attrs={'class': 'form-control'}),
        'password': forms.PasswordInput(render_value=True, attrs={'class': 'form-control'}),
        'specialite.titre': forms.TextInput( attrs={'class': 'form-control'}),

     }