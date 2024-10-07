from django.shortcuts import render
from django.urls import reverse_lazy 
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView

from . import forms


# class SignUpView(CreateView):
#     """Регистрация пользователя"""

#     template_name = "registration/registration.html"
#     form_class = forms.UserCreationForm
#     success_url = reverse_lazy("account:login")