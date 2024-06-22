from django import forms
from django.db import models

# Create your models here.

class Stagiaire(models.Model):
    numsta=models.IntegerField()
    nom=models.CharField(max_length=20)
    prenom=models.CharField(max_length=20)
    annee=models.IntegerField()
    diplome=models.CharField(max_length=10)
    sex=models.CharField(max_length=1)
    stage=models.CharField(max_length=10)


class ContactForm(forms.ModelForm):
    class Meta:
        model = Stagiaire
        fields = ['nom', 'prenom', 'annee' , 'diplome' , 'sex']




