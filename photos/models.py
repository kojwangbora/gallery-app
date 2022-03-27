from django.db import models
from pickle import FALSE, TRUE


# Create your models here.
class Location(models.Model):
    location_name =models.CharField(max_length=50, blank=TRUE, default=None)
    location_town = models.CharField(max_length=25)

    
    

