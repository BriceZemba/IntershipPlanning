from django.db import models

# Create your models here.

class Stage(models.Model):
    nostage=models.CharField(max_length=4)
    typestage=models.CharField(max_length=20)
    datedebut=models.DateField()
    datefin=models.DateField()
    nbreplace = models.IntegerField()
    nbreinscrit = models.IntegerField()
