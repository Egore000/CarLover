from django.db import models
from django.contrib.auth.models import User


class Car(models.Model):
    """Информация об автомобиле"""

    make = models.CharField(
        'Марка автомобиля',
        null=False,
        max_length=255,
    )
    model = models.CharField(
        verbose_name='Модель автомобиля',
        null=False,
        max_length=255,
    )
    year = models.IntegerField(
        verbose_name='Год выпуска',
        blank=True,
        null=True,
    )
    description = models.TextField(
        verbose_name='Описание автомобиля',
        blank=True,
        null=True,
    )
    created_at = models.DateTimeField(
        verbose_name='Дата создания',
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        verbose_name='Дата обновления',
        auto_now=True,
    )

    class Meta:
        ordering = ['make', '-created_at']
        db_table = 'cars'
    
    def __str__(self):
        return f'{self.make} {self.model} ({self.year})'


class Comment(models.Model):
    """Комментарий пользователя об автомобиле"""

    content = models.TextField(
        verbose_name='Текст',
        null=False,
    )
    created_at = models.DateTimeField(
        verbose_name='Дата и время создания комментария',
        auto_now_add=True,
    )
    car = models.ForeignKey(
        verbose_name='Автомобиль',
        to='Car',
        on_delete=models.CASCADE,
        related_name='comments',
    )
    author = models.ForeignKey(
        verbose_name='Автор комментария',
        to=User,
        on_delete=models.CASCADE,
        related_name='comments',
    )

    class Meta:
        ordering = ['-created_at']
        db_table = 'comments'
