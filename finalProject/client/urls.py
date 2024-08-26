from django.urls import path
from . import views

urlpatterns = [
    path('extraClientInfo/', views.extraClientInfo, name='client/extraClientInfo'),
]