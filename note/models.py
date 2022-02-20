from django.db import models
from matiere.models import Matiere
from etudiant.models import User
# import datetime

# Create your models here.
class Note(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    matiere = models.ForeignKey(Matiere,on_delete=models.CASCADE)
    # date_joined = datetime.date.today()
    date_joined = models.DateField(null=True)
    note_ds = models.FloatField()
    note_exam = models.FloatField()
    note_tp = models.FloatField()
    moy = models.FloatField(null=True)
    def __str__(self): 
        return self.user.name
