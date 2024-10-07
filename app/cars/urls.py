from django.urls import path
from . import views
 

app_name = 'cars'

urlpatterns = [
    path('', views.CarsListView.as_view(), name='list'),
    path('<int:pk>/', views.CarsDetailView.as_view(), name='detail'),
]