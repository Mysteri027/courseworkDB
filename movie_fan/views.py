from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import FormView, ListView, View
from .models import *
menu = [
    {'title': 'Главная', 'url_name': 'main'},
    {'title': 'Новости', 'url_name': 'news'},
]

genres = [
    {'title': 'Боевик', 'url_name': 'thriller'},
    {'title': 'Детектив', 'url_name': 'detective'},
    {'title': 'Семейный', 'url_name': 'family'},
    {'title': 'Комедия', 'url_name': 'comedy'},
]


class MainPageView(View):
    template_name = 'movie_fan/index.html'

    def get(self, request, *args, **kwargs):
        context = {
            'title': 'Главная',
            'menu': menu,
            'genres': genres,
        }
        return render(request, 'movie_fan/index.html', context=context)


class NewsPage(ListView):
    model = News
    template_name = 'movie_fan/news.html'
    context_object_name = 'news'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['genres'] = genres
        return context


class RegisterFormView(FormView):
    form_class = UserCreationForm
    success_url = 'login/'
    extra_context = {'title': 'Регистрация'}

    template_name = 'movie_fan/register.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['genres'] = genres
        return context

    def form_valid(self, form):
        form.save()
        return super(RegisterFormView, self).form_valid(form)

    def form_invalid(self, form):
        return super(RegisterFormView, self).form_valid(form)


def news(request):
    return HttpResponse('<h1> Новости </h1>')


def login(request):
    return HttpResponse('<h1> Логин </h1>')


def thriller(request):
    return HttpResponse('<h1> Боевик </h1>')


def detective(request):
    return HttpResponse('<h1> Детектив </h1>')


def family(request):
    return HttpResponse('<h1> Семейные </h1>')


def comedy(request):
    return HttpResponse('<h1> Комедия </h1>')
