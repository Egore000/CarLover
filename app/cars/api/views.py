from rest_framework import permissions, viewsets, views, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly 
from rest_framework.request import HttpRequest

from cars import models
from cars.api import serializers, permissions
from cars.api.swagger import Swagger


@Swagger.cars
class CarsViewSet(viewsets.ModelViewSet):
    """ViewSet для модели Car

    Поддерживает методы GET, POST, PUT, DELETE, PATCH
    """

    queryset = models.Car.objects.all()
    serializer_class = serializers.CarsSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, permissions.IsCarOwnerOrReadOnly, )

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class CommentsAPIView(views.APIView):
    """Представление для обработки запросов на комментарии"""

    permission_classes = (IsAuthenticatedOrReadOnly, permissions.IsCommentAuthorOrReadOnly, )

    @Swagger.get_comment
    def get(self, request: HttpRequest, car_id: int) -> Response:
        comments = models.Comment.objects.filter(car__id=car_id)
        serializer = serializers.CommentGETSerializer(comments, many=True)
        return Response(serializer.data)
    
    @Swagger.post_comment
    def post(self, request: HttpRequest, car_id: int) -> Response:
        serializer = serializers.CommentPOSTSerializer(data=request.data)

        car = models.Car.objects.get(id=car_id)
    
        if serializer.is_valid():
            comment = serializer.save(author=request.user, car=car)
            return Response({"status": "Комментарий добавлен", "id": comment.id}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)