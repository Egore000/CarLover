from django.contrib import admin
from . import models 


@admin.register(models.Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('id', 'make', 'model', 'year', 'description', 'owner')


@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):
    fields = ('content', 'car', 'author')