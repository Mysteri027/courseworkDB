from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='main'),
    path('news/', news, name='news'),
    path('registration/', registration, name='registration'),
    path('thriller/', thriller, name='thriller'),
    path('detective/', detective, name='detective'),
    path('family/', family, name='family'),
    path('comedy', comedy, name='comedy'),
]