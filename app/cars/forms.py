from django import forms
from . import models


class CarCreationForm(forms.ModelForm):
    """Форма для создания автомобиля"""
    
    class Meta:
        model = models.Car
        fields = ('make', 'model', 'year', 'description')