from django.db import models
from module.models import Module

# Create your models here.
choix = [('oui', 'OUI'), ('non', 'NON')]
class Matiere(models.Model):
    titre = models.CharField(max_length=70)
    ds = models.IntegerField()
    exam = models.IntegerField()
    tp = models.IntegerField()
    coeff = models.IntegerField(null=True)
    module = models.ForeignKey(Module, on_delete=models.CASCADE,null=True)

    
    def __str__(self):              
        return self.titre
