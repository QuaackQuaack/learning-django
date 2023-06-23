from django.db import models

# Create your models here.
class Airport(models.model):
    code = models.CharField(max_length = 3)
    city = models.CharField(max_lenght = 64)

    def __str__(self):
        return f"{self.city} ({self.city})"

class Flights(models.Model):
    origin = models.ForeignKey(Airport, on_delete = models.CASCADE,related_name= "departures") 
    destination = models.CharField( max_length = 64)
    duration = models.IntegerField()

    def __str__(self):
        return f"{self.id}: {self.origin} to {self.destination}"
