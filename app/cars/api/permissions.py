from rest_framework import permissions
from rest_framework.request import HttpRequest
from rest_framework.viewsets import ViewSet

from cars.models import Car, Comment 


class IsOwnerOrReadOnly[Obj](permissions.BasePermission):
    """Базовый класс для проверки, является ли пользователь владельцем объекта 
    или суперпользователем и предоставление ему прав на изменение/удаление записи"""

    def has_object_permission(self, request: HttpRequest, view: ViewSet, obj: Obj) -> bool:
        if request.method in permissions.SAFE_METHODS:
            return True


class IsCarOwnerOrReadOnly(IsOwnerOrReadOnly[Car]):

    def has_object_permission(self, request, view, obj):   
        read_only = super().has_object_permission(request, view, obj)
        return read_only or obj.owner == request.user or request.user.is_superuser
        

class IsCommentAuthorOrReadOnly(IsOwnerOrReadOnly[Comment]):

    def has_object_permission(self, request, view, obj):   
        read_only = super().has_object_permission(request, view, obj)
        return read_only or obj.author == request.user or request.user.is_superuser
