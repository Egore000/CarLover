from typing import Any
from django.shortcuts import get_object_or_404, redirect
from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.forms import BaseModelForm
from django.http import HttpRequest, HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic.base import ContextMixin
from django.views.generic.edit import FormMixin
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required

from . import models, forms 


class CarsListView(ListView):
    """Список автомобилей"""

    model = models.Car
    template_name = 'cars/list.html'
    context_object_name = 'cars'


class CarsDetailView(DetailView, FormMixin):
    """Детальное отображение информации об автомобиле"""

    model = models.Car
    template_name = 'cars/detail.html'  
    form_class = forms.CommentCreationForm
    
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
    

class UserCarsListView(LoginRequiredMixin, ListView):
    """Список автомобилей пользователя"""

    model = models.Car
    template_name = 'cars/list.html'
    context_object_name = 'cars'

    def get_queryset(self) -> QuerySet[Any]:
        return models.Car.objects.filter(owner=self.request.user)


@login_required
@require_http_methods(['POST'])
def post_comment(request: HttpRequest, pk: int) -> HttpResponse:
    """Отправка комментария"""
    
    form = forms.CommentCreationForm(request.POST)
    car = get_object_or_404(models.Car, pk=pk)

    if form.is_valid():
        comment = models.Comment()

        comment.content = form.cleaned_data.get('content')
        comment.car = car
        comment.author = request.user

        comment.save()
    
    return redirect(car.get_absolute_url())