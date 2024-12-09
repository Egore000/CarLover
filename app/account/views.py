from django.http import HttpResponse, HttpRequest 
from django.shortcuts import render
from django.contrib.auth.models import User

from . import forms


def register(request: HttpRequest) -> HttpResponse:
    """Регистрация пользователя"""

    if request.method == 'POST':
        form = forms.UserRegistrationForm(request.POST)

        if form.is_valid():
            user: User = form.save(commit=False)

            user.set_password(
                form.cleaned_data.get('password')
            )
            user.save()

            return render(request, 
                          'account/register_done.html',
                          context={'user': user}
            )
    else:
        form = forms.UserRegistrationForm()
    
    return render(request, 
                  'account/register.html',
                  context={'form': form})
