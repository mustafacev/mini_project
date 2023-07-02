from django.contrib import admin

# Register your models here.
from .models import TruckBrand , TruckModel , FavoriteTrucksList
admin.site.register(TruckBrand)
admin.site.register(TruckModel)
admin.site.register(FavoriteTrucksList)