from typing import Any
from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from . import models, forms 


class CarsListView(ListView):
    """Список автомобилей"""

    model = models.Car
    template_name = 'cars/list.html'
    context_object_name = 'cars'


class CarsDetailView(DetailView):
    """Детальное отображение информации об автомобиле"""

    model = models.Car
    template_name = 'cars/detail.html'  
    
    def get_queryset(self) -> QuerySet[Any]:
        return models.Car.objects.prefetch_related('comments__author').all()


class CarsCreateView(LoginRequiredMixin, CreateView):
    """Создание нового автомобиля"""
    
    model = models.Car
    form_class = forms.CarCreationForm
    success_url = reverse_lazy('cars:list')
    template_name = 'cars/add_new.html'


class CarsUpdateView(PermissionRequiredMixin, UpdateView):
    """Обновление информации об автомобиле"""
    
    model = models.Car
    fields = ('make', 'model', 'year', 'description')
    template_name = 'cars/add_new.html'
    success_url = reverse_lazy('cars:list')
    
    def has_permission(self) -> bool:
        obj = self.get_object()
        if self.request.user is obj.owner:
            return True
        return False