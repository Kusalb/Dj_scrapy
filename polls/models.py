from django.db import models

# Create your models here.
class Tarkari(models.Model):
    name = models.CharField(max_length=150)
    unit = models.CharField(max_length=150)
    maximum = models.CharField(max_length=150)
    minimum = models.CharField(max_length=150)
    average = models.CharField(max_length=150)
    datee = models.CharField(max_length=150)

    class Meta:
        verbose_name = "tarkari"
