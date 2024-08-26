from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('users/', include('users.urls')),
    path('client/', include('client.urls')),
    path('restaurant/', include('restaurant.urls')),
    path('admin/', admin.site.urls),
]