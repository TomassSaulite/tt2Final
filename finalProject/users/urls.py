from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.urls import include, path
urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.custom_login_view, name='login'),
    path('loginSuccessful/', views.loginSuccessful, name='loginSuccessful'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logouts, name='logout'),
]