from typing import Any
from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.forms import BaseModelForm
from django.http import HttpRequest, HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic.base import ContextMixin 

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


class CarsCreateView(LoginRequiredMixin, CreateView, ContextMixin):
    """Создание нового автомобиля"""
    
    model = models.Car
    form_class = forms.CarCreationForm
    success_url = reverse_lazy('cars:list')
    template_name = 'cars/add_new.html'
    extra_context = {'title': 'Добавить авто'}

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        car = form.save(commit=False)
        car.owner = self.request.user
        return super().form_valid(form)


class CarsUpdateView(PermissionRequiredMixin, UpdateView, ContextMixin):
    """Обновление информации об автомобиле"""
    
    model = models.Car
    fields = ('make', 'model', 'year', 'description')
    template_name = 'cars/add_new.html'
    success_url = reverse_lazy('cars:list')
    extra_context = {'title': 'Изменение авто'}
    
    def has_permission(self) -> bool:
        obj = self.get_object()
        print(obj.owner, self.request.user)
        if self.request.user == obj.owner:
            return True
        return False