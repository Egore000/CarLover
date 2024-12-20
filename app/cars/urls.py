from django.urls import path
from . import views
 

app_name = 'cars'

urlpatterns = [
    path('', views.CarsListView.as_view(), name='list'),
    path('<int:pk>/', views.CarsDetailView.as_view(), name='detail'),
    path('create/', views.CarsCreateView.as_view(), name='create'),
    path('edit/<int:pk>', views.CarsUpdateView.as_view(), name='edit'),
    path('<int:pk>/comment', views.post_comment, name='post_comment'),
    path('my/', views.UserCarsListView.as_view(), name='my_cars_list'),
]

