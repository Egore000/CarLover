from rest_framework import permissions, viewsets, views, status
from rest_framework.response import Response
from rest_framework.request import HttpRequest 

from drf_spectacular.utils import extend_schema_view, extend_schema, OpenApiResponse

from cars import models
from cars.api import serializers  


@extend_schema_view(
    list=extend_schema(
        description="Выводит список всех автомобилей.",
        responses={
            200: OpenApiResponse(
                response=serializers.CarsSerializer(many=True), 
                description="Данные получены"
            ),
        }
    ),
    create=extend_schema(
        description="Добавление информации об автомобиле.",
        responses={
            201: OpenApiResponse(description="Создано успешно"),
            401: OpenApiResponse(description="Ошибки валидации"),
        }
    ),
    retrieve=extend_schema(
        description="Вывод подробной информации о конкретном автомобиле.",
        responses={
            200: OpenApiResponse(
                response=serializers.CarsSerializer(), 
                description="Информация об автомобиле."
            ),
            404: OpenApiResponse(description="Данные об автомобиле не найдены"),
        }
    ),
    update=extend_schema(
        description="Изменение информации об автомобиле.",
    ),
    partial_update=extend_schema(
        description="Частичное изменение информации об автомобиле.",
    ),
    destroy=extend_schema(
        description="Удаление информации об автомобиле.",
        responses={
            200: OpenApiResponse(description="Автомобиль успешно удалён"),
            404: OpenApiResponse(description="Автомобиль не найден"),
            400: OpenApiResponse(description="ID автомобиля не предоставлен")
        }
    )
)
class CarsViewSet(viewsets.ModelViewSet):
    """ViewSet для модели Car

    Поддерживает методы GET, POST, PUT, DELETE, PATCH
    """

    queryset = models.Car.objects.all()
    serializer_class = serializers.CarsSerializer
    permission_classes = (permissions.IsAuthenticated, )

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)



# class CommentsListAPIView(generics.ListAPIView):
#     """Список комментариев для определённого автомобиля"""

#     serializer_class = serializers.CommentSerializer

#     def get_queryset(self):
#         return models.Comment.objects.filter(car__id=self.kwargs.get('car_id'))
    

# class CommentsCreateAPIView(generics.CreateAPIView):
#     """Добавление комментария"""

#     serializer_class = serializers.CommentPOSTSerializer
#     permission_classes = (permissions.IsAuthenticated, )

#     def perform_create(self, serializer):
#         car = models.Car.objects.get(id=self.kwargs.get('car_id'))
#         serializer.save(
#             author=self.request.user,
#             car=car
#         )


class CommentsAPIView(views.APIView):
    @extend_schema(
        summary="Вывод всех комментариев об автомобиле",
        responses={
            201: OpenApiResponse(response=serializers.CommentSerializer, description="Список всех комментариев об авто"),
        }
    )
    def get(self, request: HttpRequest, car_id: int) -> Response:
        comments = models.Comment.objects.filter(car__id=car_id)
        serializer = serializers.CommentSerializer(comments, many=True)
        return Response(serializer.data)
    
    @extend_schema(
        summary="Создание комментария",
        request=serializers.CommentPOSTSerializer,
        responses={
            201: OpenApiResponse(response=serializers.CommentPOSTSerializer, description="Комментарий добавлен"),
            400: OpenApiResponse(description="Ошибки валидации")
        }
    )
    def post(self, request: HttpRequest, car_id: int) -> Response:
        serializer = serializers.CommentPOSTSerializer(data=request.data)

        car = models.Car.objects.get(id=car_id)
    
        if serializer.is_valid():
            comment = serializer.save(author=request.user, car=car)
            return Response({"status": "Комментарий добавлен", "id": comment.id}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)