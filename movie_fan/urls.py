from django.urls import path

from .views import *

urlpatterns = [
    path('', MainPageView.as_view(), name='main'),
    path('news/', NewsPage.as_view(), name='news'),
    path('register/', RegisterFormView.as_view(), name='register'),
    path('login/', LoginFormView.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('movies/',MoviesPage.as_view(), name='all_movies'),

    path('reviews/<int:movies_id>/', get_reviews, name='reviews'),
    path('add_like_review/<int:review_id>/', add_like_review, name='add_like_review'),
    path('add_dislike_review/<int:review_id>/', add_dislike_review, name='add_dislike_review'),
    path('add_review/<int:movies_id>/', add_review, name='add_review'),



    path('thriller/', thriller, name='thriller'),
    path('detective/', detective, name='detective'),
    path('family/', family, name='family'),
    path('comedy', comedy, name='comedy'),
]