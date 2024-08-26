from django.urls import path
from . import views

urlpatterns = [
    path('extraRestaurantInfo/', views.extraRestaurantInfo, name='restaurant/extraRestaurantInfo'),
]
