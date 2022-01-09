from django.urls import path

from .views import *

urlpatterns = [
    path('', MainPageView.as_view(), name='main'),
    path('news/', NewsPage.as_view(), name='news'),
    path('register/', RegisterFormView.as_view(), name='register'),
    path('login/', login, name='login'),
    path('thriller/', thriller, name='thriller'),
    path('detective/', detective, name='detective'),
    path('family/', family, name='family'),
    path('comedy', comedy, name='comedy'),
]