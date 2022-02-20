
from django.db import models
from specialite.models import Specialite
from matiere.models import Matiere
# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=70)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    age = models.IntegerField(null=True)
    tel = models.IntegerField(null=True)
    niveau = models.IntegerField(null=True)
    specialite = models.ForeignKey(Specialite, on_delete=models.CASCADE,null=True)
    matieres = models.ManyToManyField(Matiere)

    def get_matieres(self):
        return "\n".join([m.matiere for m in self.matieres.all()])
 
    def __str__(self):             
        return self.name




