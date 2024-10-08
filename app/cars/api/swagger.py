from django.utils.translation import gettext_lazy as _ 

from drf_spectacular.utils import extend_schema, extend_schema_view, OpenApiResponse, OpenApiRequest

from cars.api import serializers 


class Swagger:
    """
    Подключение swagger к проекту и обобрачивание представлений в 
    декораторы
    """

    @classmethod
    def cars(cls, extended):
        return extend_schema_view(
            list=extend_schema(
                description=_("Выводит список всех автомобилей."),
                responses={
                    200: OpenApiResponse(
                        response=serializers.CarsSerializer(many=True), 
                        description=_("Данные получены")
                    ),
                }
            ),
            create=extend_schema(
                description=_("Добавление информации об автомобиле."),
                responses={
                    201: OpenApiResponse(description=_("Создано успешно")),
                    401: OpenApiResponse(description=_("Ошибки валидации")),
                }
            ),
            retrieve=extend_schema(
                description=_("Вывод подробной информации о конкретном автомобиле."),
                responses={
                    200: OpenApiResponse(
                        response=serializers.CarsSerializer(), 
                        description=_("Информация об автомобиле.")
                    ),
                    404: OpenApiResponse(description=_("Данные об автомобиле не найдены")),
                }
            ),
            update=extend_schema(
                description=_("Изменение информации об автомобиле."),
            ),
            partial_update=extend_schema(
                description=_("Частичное изменение информации об автомобиле."),
            ),
            destroy=extend_schema(
                description=_("Удаление информации об автомобиле."),
                responses={
                    200: OpenApiResponse(description=_("Автомобиль успешно удалён")),
                    404: OpenApiResponse(description=_("Автомобиль не найден")),
                    400: OpenApiResponse(description=_("ID автомобиля не предоставлен"))
                }
            )
        )(extended)

    @classmethod
    def get_comment(cls, extended):
        return extend_schema(
            description=_("Вывод всех комментариев об автомобиле"),
            responses={
                201: OpenApiResponse(
                    response=serializers.CommentGETSerializer, 
                    description=_("Список всех комментариев об авто")
                ),
            }
        )(extended)
    
    @classmethod
    def post_comment(cls, extended):
        return extend_schema(
            description=_("Создание комментария"),
            request=serializers.CommentPOSTSerializer,
            responses={
                201: OpenApiResponse(
                    response=serializers.CommentPOSTSerializer, 
                    description=_("Комментарий добавлен")
                ),
                400: OpenApiResponse(description=_("Ошибки валидации"))
            }
        )(extended)