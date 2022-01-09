from django.contrib import admin
from .models import Movie, Review, Director, News


admin.site.register(Movie)
admin.site.register(Review)
admin.site.register(Director)
admin.site.register(News)