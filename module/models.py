from django.db import models
from specialite.models import Specialite
# Create your models here.
class Module(models.Model):
    title = models.CharField(max_length=70)
    coeff = models.IntegerField(null=True)
    specialite = models.ForeignKey(Specialite, on_delete=models.CASCADE,null=True)
    def __str__(self): 
        return self.title
