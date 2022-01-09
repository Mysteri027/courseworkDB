from django.contrib import admin
from django.urls import path

from movie_fan.views import index
from django.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('movie_fan.urls')),
]
