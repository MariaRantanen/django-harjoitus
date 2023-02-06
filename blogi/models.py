from django.db import models

class Postaus(models.Model):
    otsikko = models.CharField(max_length=200)
    teksti = models.TextField()


