from django.db import models

# Create your models here.
class Airport(models.Model):
    code = models.CharField(max_length=3)
    city = models.CharField(max_length=64)

    def __str__(self) -> str:
        return f"{self.city} ({self.code})"


class Flight(models.Model):
    origin = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="departures")  # if I'm an Airport, I want to check every flight that has me as origin
    destination = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="arrivals")  # if I'm an Aiport, I want to check every flight that has me as destination
    duration = models.IntegerField()
    
    def __str__(self) -> str:
        return f"{self.id}: {self.origin} to {self.destination}"


