from django.urls import path, include
from rest_framework.routers import DefaultRouter

from cars.api import views


app_name = 'api_cars'

router = DefaultRouter()
router.register(r'cars', views.CarsViewSet, basename='cars')

urlpatterns = [
    path('', include(router.urls)),
    path('cars/<int:car_id>/comments/', views.CommentsAPIView.as_view(), name='comments'),
]
