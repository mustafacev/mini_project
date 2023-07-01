from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('about/', views.About.as_view(), name="about"), 
    path('trucks/',views.TrucksList.as_view(), name="trucks_list"),
    path('custom/',views.CustomList.as_view(), name="custom_list"),
]