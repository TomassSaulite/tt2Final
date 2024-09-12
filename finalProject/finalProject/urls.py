from django.contrib import admin
from django.urls import include, path
from django.shortcuts import redirect

urlpatterns = [
    path('', lambda request: redirect('users/', permanent=True)),
    path('users/', include('users.urls')),
    path('client/', include('client.urls')),
    path('restaurant/', include('restaurant.urls')),
    path('admin/', admin.site.urls),
]