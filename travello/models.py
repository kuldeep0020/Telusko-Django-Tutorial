from django.db import models


# Create your models here.
class Destination(models.Model):
    destId = models.IntegerField()
    name = models.TextField()
    img = models.TextField()
    desc = models.CharField(max_length=60)
    price = models.IntegerField()
