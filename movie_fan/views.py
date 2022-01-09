from django.shortcuts import render
from django.http import HttpResponse

# menu = ['Главная','Новости', 'Регистрация']
menu = [
        {'title': 'Главная', 'url_name': 'main'},
        {'title': 'Новости', 'url_name': 'news'},
        {'title':'Регистрация', 'url_name': 'registration'}
]

genres = [
        {'title': 'Боевик', 'url_name': 'thriller'},
        {'title': 'Детектив', 'url_name': 'detective'},
        {'title':'Семейный', 'url_name': 'family'},
        {'title':'Комедия', 'url_name': 'comedy'},
]


def index(request):
    context = {
        'title': 'Главная',
        'menu': menu,
        'genres': genres,
    }
    return render(request, 'movie_fan/index.html', context=context)


def news(request):
    return HttpResponse('<h1> Новости </h1>')


def registration(request):
    return HttpResponse('<h1> Регистрация </h1>')


def thriller(request):
    return HttpResponse('<h1> Боевик </h1>')


def detective(request):
    return HttpResponse('<h1> Детектив </h1>')


def family(request):
    return HttpResponse('<h1> Семейные </h1>')


def comedy(request):
    return HttpResponse('<h1> Комедия </h1>')
