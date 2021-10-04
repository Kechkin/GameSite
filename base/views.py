from django.shortcuts import render, redirect
from django.views import View
from .forms import ReviewForm
from .models import Game, Review, Company, PersonGame, Genre


class FilterGenres:
    """Вывод все жанров"""
    def get_genres(self):
        return Genre.objects.all()


class Home(FilterGenres, View):
    """Список всех статей с играми"""
    def get(self, request):
        games = Game.objects.filter(draft=False)
        return render(request, 'base/index.html', {'games': games, 'genres': FilterGenres.get_genres(self)})


class DetailGame(FilterGenres, View):
    """Подробное описание статьи"""
    def get(self, request, slug):
        game = Game.objects.get(slug=slug)
        comments = Review.objects.filter(game__slug=slug)
        return render(request, 'base/detail_game.html', {'game': game, 'comments': comments,
                                                         'genres': FilterGenres.get_genres(self)})


class AddReview(FilterGenres, View):
    """Добавление комментария"""
    def post(self, request, slug):
        game = Game.objects.get(slug=slug)
        form = ReviewForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.game = game
            form.save()
        return redirect(f'/{slug}')


class GameCompany(FilterGenres, View):
    """Описание компании разработчиков"""
    def get(self, request, slug):
        company = Company.objects.get(slug=slug)
        return render(request, 'base/company.html', {'company': company, 'genres': FilterGenres.get_genres(self)})


class GetPerson(FilterGenres, View):
    """Описание главного персонажа"""
    def get(self, request, slug):
        person = PersonGame.objects.get(slug=slug)
        return render(request, 'base/person_game.html', {'person': person, 'genres': FilterGenres.get_genres(self)})


class FilterGenre(FilterGenres, View):
    """Выборка по жанрам"""
    def get(self, request, pk):
        games = Game.objects.filter(genres=pk)
        return render(request, 'base/genre.html', {'games': games, 'genres': FilterGenres.get_genres(self)})


class SearchGame(FilterGenres, View):
    """Поиск статей про игры"""
    def get(self, request):
        games = Game.objects.filter(title__icontains=request.GET.get('text'))
        search = request.GET.get('text')
        return render(request, 'base/search.html', {'games': games, 'genres': FilterGenres.get_genres(self),
                                                    'search': search})
