from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('about/', views.About.as_view(), name="about"), 
    path('trucks/',views.TrucksList.as_view(), name="trucks_list"),
    path('custom/',views.CustomList.as_view(), name="custom_list"),
    path('trucks/new/', views.TrucksCreate.as_view(), name="trucks_create"),
    path('trucks/<int:pk>/', views.TruckDetail.as_view(), name="truck_detail"),
    path('trucks/<int:pk>/update/',views.TruckUpdate.as_view(), name="truck_update"),
    path('trucks/<int:pk>/delete',views.TruckDelete.as_view(), name="truck_delete"),
    path('trucks/<int:pk>/truckmodel/new/', views.TruckModelCreate.as_view(), name="truck_model_create"),
    path('favoritetruckslists/<int:pk>/truckmodel/<int:truck_model_pk>/', views.FavoriteTrucksListTruckModelAssoc.as_view(), name="favorite_trucks_list_truck_model_assoc"),
]