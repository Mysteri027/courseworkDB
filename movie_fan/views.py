from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import ListView, View, CreateView

from .forms import RegisterUserForm, LoginUserForm
from .models import *
from .utils import *


class MainPageView(View):
    template_name = 'movie_fan/index.html'

    def get(self, request, *args, **kwargs):
        context = {
            'title': 'Главная',
            'menu': menu,
            'top_movies': set_top_movies(),
        }
        return render(request, 'movie_fan/index.html', context=context)


class NewsPage(ListView):
    model = News
    template_name = 'movie_fan/news.html'
    context_object_name = 'news'
    extra_context = {'title': 'Новости кино'}


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['top_movies'] = set_top_movies()
        return context


class MoviesPage(ListView):
    model = Movie
    template_name = 'movie_fan/movies.html'
    context_object_name = 'movies'
    extra_context = {'title': 'Фильмы'}


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['top_movies'] = set_top_movies()
        return context


class RegisterFormView(CreateView):
    form_class = RegisterUserForm
    success_url = reverse_lazy('login')
    extra_context = {'title': 'Регистрация'}

    template_name = 'movie_fan/register.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['top_movies'] = set_top_movies()
        return context

    def form_valid(self, form):
        form.save()
        return super(RegisterFormView, self).form_valid(form)

    def form_invalid(self, form):
        return super(RegisterFormView, self).form_valid(form)


class LoginFormView(LoginView):
    form_class = LoginUserForm
    template_name = 'movie_fan/login.html'
    success_url = reverse_lazy('news')
    extra_context = {'title': 'Логин'}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['top_movies'] = set_top_movies()
        return context


def get_reviews(request, movies_id):
    reviews = Review.objects.filter(movie_id=movies_id)
    movie = Movie.objects.get(pk=movies_id)
    reviews_count = Review.objects.filter(movie_id=movies_id).count()
    context = {
            "reviews": reviews,
            "reviews_count": reviews_count,
            "title": "Рецензии",
            "menu": menu,
            "top_movies": set_top_movies(),
            "movie": movie,
        }
    return render(request, "movie_fan/reviews.html", context=context)


def add_like_review(request, review_id):
    review = Review.objects.get(id=review_id)
    review.likes_count += 1
    review.save()
    return HttpResponseRedirect('/reviews/' + str(review.movie_id.id))



def add_dislike_review(request, review_id):
    review = Review.objects.get(id=review_id)
    review.dislikes_count += 1
    review.save()
    return HttpResponseRedirect('/reviews/' + str(review.movie_id.id))


def add_review(request, movies_id):
    review = Review()
    review.text = request.POST.get('review_text')
    review.likes_count = 0
    review.dislikes_count = 0
    review.movie_id = Movie.objects.get(id=movies_id)
    review.save()

    return HttpResponseRedirect('/reviews/' + str(review.movie_id.id))


def logout_user(request):
    logout(request)
    return redirect('login')


def set_top_movies():
    movies = Movie.objects.order_by('-rating')
    return movies


def get_move_by_id(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    context = {
        'title': f'{movie.name}',
        'menu': menu,
        'top_movies': set_top_movies(),
        'movie': movie,
    }
    return render(request, "movie_fan/movie.html", context=context)


def search(request):
    context = {
        'title': f'Поиск',
        'menu': menu,
        'top_movies': set_top_movies(),
    }
    return render(request, "movie_fan/search.html", context=context)


def check_search_bar(request):
    if request.method == 'GET':
        search_input = request.GET["search_name"]

        movie_names = Movie.objects.values_list('name', flat=True)
        directors_names = Director.objects.values_list('full_name', flat=True)

        if search_input in movie_names:
            movie = Movie.objects.get(name=search_input)
            context = {
                'title': f'{movie.name}',
                'menu': menu,
                'top_movies': set_top_movies(),
                'movie': movie,
            }
            return HttpResponseRedirect('/movie/' + str(movie.id))

        elif search_input in directors_names:
            movies = Movie.objects.filter(director__full_name=search_input)
            print(movies)
            context = {
                'title': f'Фильмы режиссёра {search_input}',
                'menu': menu,
                'top_movies': set_top_movies(),
                'movies': movies,
            }
            return render(request, "movie_fan/directors_movies.html", context=context)

        else:
            return HttpResponse('Error', content_type='text/html')
