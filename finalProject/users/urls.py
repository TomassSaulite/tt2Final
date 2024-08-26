from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.custom_login_view, name='login'),
    path('loginSuccessful/', views.loginSuccessful, name='loginSuccessful'),
    path('signup/', views.signup, name='signup'),
]