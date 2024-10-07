from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from . import models 


class CarsListView(ListView):
    """Список автомобилей"""

    model = models.Car
    template_name = 'cars/index.html'
    context_object_name = 'cars'


class CarsDetailView(DetailView):
    """Детальное отображение информации об автомобиле"""

    model = models.Car
    template_name = 'cars/detail.html'  


