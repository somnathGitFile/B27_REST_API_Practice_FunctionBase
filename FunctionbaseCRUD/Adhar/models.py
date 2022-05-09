from statistics import mode
from django.db import models

# Create your models here.
class Adharcard(models.Model):
    aid = models.IntegerField()
    aname = models.CharField(max_length=100)
    anumber = models.IntegerField()
    aadd = models.CharField(max_length=200)

    def __str__(self):
        return self.aname

