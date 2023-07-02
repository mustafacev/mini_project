from django.db import models
import time


# Create your models here.

class TruckBrand(models.Model):

    name = models.CharField(max_length=100)
    img = models.CharField(max_length=250)
    info = models.TextField(max_length=500, default='info')
    verified_truck = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

class TruckModel(models.Model):

    name = models.CharField(max_length=150)
    max_speed = models.IntegerField(default=0)
    truck_brand = models.ForeignKey(TruckBrand, on_delete=models.CASCADE, related_name="truck_model")

    def __str__(self):
        return self.name
    
    def get_length(self):
        return time.strftime("%-M:%S", time.gmtime(self.max_speed))
    
class FavoriteTrucksList(models.Model):

    name = models.CharField(max_length=150)
    truck_model = models.ManyToManyField(TruckModel)

    def __str__(self):
        return self.name