from django.db import models

# Create your models here.
class Sdr(models.Model):
    ip = models.GenericIPAddressField()
    loc_x = models.FloatField(max_length=10)
    loc_y = models.FloatField(max_length=10)
    name = models.CharField(max_length=20)
