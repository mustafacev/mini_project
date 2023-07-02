from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from .models import TruckBrand, TruckModel
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from django.shortcuts import redirect
# Create your views here.


class Home(TemplateView):
    def get(self, request):
        return HttpResponse(" Home")


class About(TemplateView):
    template_name = "about.html"


# class Truck:
#     def __init__(self, name, image, info):
#         self.name = name
#         self.image = image
#         self.info = info


# trucks = [
#     Truck("1964 Chevrolet C/K 10 Pickup Truck", "https://static.cargurus.com/images/forsale/2023/06/23/01/38/1964_chevrolet_c_k_10-pic-7989152919389611161-1024x768.jpeg",
#           "LS-Powered C10 Restomod 5.3L LS V8 6spd Automatic A/C RideTech Suspension Price $$ 129,999 "),
#     Truck("1966 Ford F-250 4x4", "https://static.cargurus.com/images/forsale/2023/06/01/23/05/1966_ford_f-250-pic-7852627915320570323-1024x768.jpeg",
#           "1966 Ford F-250 4x4 Price $21,950 "),
#     Truck("1974 Ford F-100 Counts Kustoms", "https://images.hotrodhotline.com/ui/6/27/aemX12e8vz.jpg",
#           "1974 Ford F100 460ci V8 Cobra Engine Automatic Transmission RWD Black / Grey Exterior Price $$69,842 "),
#     Truck("1954 Chevrolet 3600", "https://cdn.dealeraccelerate.com/fusion/1/327/12235/1920x1440/1954-chevrolet-3600",
#           "This fully restored truck is a showstopper, with a gleaming exterior that sparkles in the sun and a beautifully refurbished cabin Price $37,999 "),
# ]


class TrucksList(TemplateView):
    template_name = "trucks_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get("name")
        if name != None:
            context["trucks"] = TruckBrand.objects.filter(name__icontains=name)
            # We add a header context that includes the search param
            context["header"] = f"Searching for {name}"
        else:
            context["trucks"] = TruckBrand.objects.all()
            # default header for not searching
            context["header"] = "Truck list"
        return context


class CustomList(TemplateView):
    template_name = "custom_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["customs"] = customs
        return context


class Custom:
    def __init__(self, name, description):
        self.name = name
        self.description = description


customs = [
    Custom("James Buckalew’s Black Betty GMC",
           "James Buckalew GMC 1972 Material / Color: Vinyl / Red."),
    Custom("Wild Chevy Crew Cab Dually Truck Is Reborn As A Rad Open-Roof Limo",
           "It started life as a 1980 Chevrolet heavy-duty crew-cab  pickup truck. ")
]


class TrucksCreate(CreateView):
    model = TruckBrand
    fields = ['name', 'img', 'info', 'verified_truck']
    template_name = "trucks_create.html"
    success_url = "/trucks/"


class TruckDetail(DetailView):
    model = TruckBrand
    template_name = "truck_detail.html"


class TruckUpdate(UpdateView):
    model = TruckBrand
    fields = ['name', 'img', 'info', 'verified_truck']
    template_name = "truck_update.html"
    success_url = "/trucks/"


class TruckDelete(DeleteView):
    model = TruckBrand
    template_name = "truck_delete_confirmation.html"
    success_url = "/trucks/"


class TruckModelCreate(View):

    def post(self, request, pk):
        name = request.POST.get("name")
        max_speed = request.POST.get("max_speed")
        truck_brand = TruckBrand.objects.get(pk=pk)
        TruckModel.objects.create(
            name=name, max_speed=max_speed, truck_brand=truck_brand)
        return redirect('truck_detail', pk=pk)
