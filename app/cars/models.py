from typing import Iterable
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class Car(models.Model):
    """Информация об автомобиле"""

    make = models.CharField(
        verbose_name=_('Марка автомобиля'),
        null=False,
        max_length=255,
    )
    model = models.CharField(
        verbose_name=_('Модель автомобиля'),
        null=False,
        max_length=255,
    )
    year = models.IntegerField(
        verbose_name=_('Год выпуска'),
        blank=True,
        null=True,
    )
    description = models.TextField(
        verbose_name=_('Описание автомобиля'),
        blank=True,
        null=True,
    )
    created_at = models.DateTimeField(
        verbose_name=_('Дата создания'),
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        verbose_name=_('Дата обновления'),
        auto_now=True,
    )
    owner = models.ForeignKey(
        verbose_name=_('Владелец'),
        to=User,
        on_delete=models.CASCADE,
        related_name='owners',
        null=False,
    )

    class Meta:
        ordering = ['make', '-created_at']
        db_table = 'cars'
        verbose_name = _('Автомобиль')
        verbose_name_plural = _('Автомобили')
    
    def __str__(self):
        return f'{self.make} {self.model} ({self.year})'
    
    def get_absolute_url(self):
        return reverse('cars:detail', kwargs={'pk': self.id})


class Comment(models.Model):
    """Комментарий пользователя об автомобиле"""

    content = models.TextField(
        verbose_name=_('Текст'),
        null=False,
    )
    created_at = models.DateTimeField(
        verbose_name=_('Дата и время создания комментария'),
        auto_now_add=True,
    )
    car = models.ForeignKey(
        verbose_name=_('Автомобиль'),
        to='Car',
        on_delete=models.CASCADE,
        related_name='comments',
    )
    author = models.ForeignKey(
        verbose_name=_('Автор комментария'),
        to=User,
        on_delete=models.CASCADE,
        related_name='comments',
    )

    class Meta:
        ordering = ['-created_at']
        db_table = 'comments'
        verbose_name = _('Комментарий')
        verbose_name_plural = _('Комментарии')
    