from datetime import datetime
from typing import Any

from rest_framework import serializers

from cars import models 


class CarsSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Car"""
    
    class Meta:
        model = models.Car
        fields = ('id', 'make', 'model', 'year', 'description', 'created_at', 'updated_at')

    def validate_year(self, year: Any):
        """Валидация входного значения года"""
        
        if not isinstance(year, int):
            raise serializers.ValidationError("Неверный тип значения года")
        
        current_year = datetime.now().year
        if year >= current_year:
            raise serializers.ValidationError(f"Год не может быть больше, чем {current_year}")
        return year


class CommentGETSerializer(serializers.ModelSerializer):
    """Сериализатор для получения комментариев"""

    class Meta:
        model = models.Comment
        fields = ('id', 'content', 'car', 'author')


class CommentPOSTSerializer(serializers.ModelSerializer):
    """Сериализатор для добавления комментариев"""

    class Meta:
        model = models.Comment
        fields = ('content', )