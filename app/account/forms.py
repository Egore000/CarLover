from django import forms
from django.contrib.auth.models import User

from django.utils.translation import gettext_lazy as _


class UserRegistrationForm(forms.ModelForm):
    """Форма создания аккаунта пользователя"""
    
    password = forms.CharField(
        label=_('Пароль'),
        widget=forms.PasswordInput,
    )
    password2 = forms.CharField(
        label=_('Повторите пароль'),
        widget=forms.PasswordInput,
    )

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')

    def clean_password2(self):
        password, password2 = self.cleaned_data['password'], self.cleaned_data['password2']

        if password != password2:
            raise forms.ValidationError(_('Пароли не совпадают!'))
        return password2
    