from typing import Any, Mapping
from django import forms
from django.forms.renderers import BaseRenderer
from django.forms.utils import ErrorList
from . import models


class CarCreationForm(forms.ModelForm):
    """Форма для создания автомобиля"""
    
    class Meta:
        model = models.Car
        fields = ('make', 'model', 'year', 'description')


class CommentCreationForm(forms.ModelForm):
    """Форма для создания комментария"""
    
    class Meta:
        model = models.Comment
        fields = ('content', )