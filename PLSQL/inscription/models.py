from django.db import models

# Create your models here.
class Inscription(models.Model):
    codestage=models.IntegerField()
    numstagiaire=models.IntegerField()
    dateinsc=models.IntegerField()
    statusinscr=models.CharField(max_length=20)
    codeposition=models.IntegerField()