from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import FormView, ListView, View
from .models import *
from .utils import *


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
    extra_context = {'title': 'Новости кино'}


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['genres'] = genres
        return context


class MoviesPage(ListView):
    model = Movie
    template_name = 'movie_fan/movies.html'
    context_object_name = 'movies'
    extra_context = {'title': 'Фильмы'}


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



def get_reviews(request, movies_id):
    reviews = Review.objects.filter(movie_id=movies_id)
    movie = Movie.objects.get(pk=movies_id)
    reviews_count = Review.objects.filter(movie_id=movies_id).count()
    context = {
            "reviews": reviews,
            "reviews_count": reviews_count,
            "title": "Рецензии",
            "menu": menu,
            "genres": genres,
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
    if request.method == "POST":
        review = Review()
        review.text = request.POST.get('review_text')
        review.likes_count = 0
        review.dislikes_count = 0
        review.save()
        return HttpResponseRedirect('/reviews/' + str(review.movie_id.id))


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
