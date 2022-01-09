import datetime
from django.db import models


class Director(models.Model):
    full_name = models.CharField(max_length=255)
    birth_date = models.DateField(default='1970-01-01')
    photo = models.ImageField()
    bio = models.CharField(max_length=255)


class Movie(models.Model):
    name = models.CharField(max_length=50)
    mark = models.IntegerField()
    rating = models.FloatField()
    poster = models.ImageField()
    trailer = models.CharField(max_length=255)
    production_year = models.IntegerField()
    country = models.CharField(max_length=50)
    genre = models.CharField(max_length=50)
    director = models.ForeignKey(Director, on_delete=models.CASCADE)
    producer = models.CharField(max_length=50)


class Review(models.Model):
    text = models.CharField(max_length=255)
    date = models.DateField(default=datetime.date.today())
    likes_count = models.IntegerField()
    dislikes_count = models.IntegerField()
    movie_id = models.ForeignKey(Movie, on_delete=models.CASCADE)


class News(models.Model):
    title = models.CharField(max_length=50)
    text = models.CharField(max_length=255)
