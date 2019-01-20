from django.db import models

# Create your models here.
class Weather(models.Model):
    wtype = models.CharField(max_length=20)
    date = models.DateField()
    value = models.DecimalField(max_digits=8, decimal_places=3)
    location = models.CharField(max_length=20)
