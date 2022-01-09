from django.shortcuts import render
from django.http import HttpResponse

menu = ['Главная','Новости', 'Топ 10  фильмов', 'Регистрация']

def index(request):
    return render(request, 'movie_fan/index.html', {'title': 'Главная', 'menu': menu})

