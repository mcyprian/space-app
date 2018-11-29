from django.db import models


class Moon(models.Model):
    name = models.CharField(max_length=255, null=False)
    planet = models.CharField(max_length=255, null=False)
    discovered = models.DateField()
    volume = models.FloatField()
