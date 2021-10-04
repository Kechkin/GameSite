from django.urls import path

from . import views


urlpatterns = [
    path('',  views.Home.as_view(), name='home'),
    path('<slug:slug>/',  views.DetailGame.as_view(), name='detail_game'),
    path('/search',  views.SearchGame.as_view(), name='search'),
    path('genre/<int:pk>/', views.FilterGenre.as_view(), name='genre'),
    path('company/<slug:slug>/', views.GameCompany.as_view(), name='game_company'),
    path('person/<slug:slug>/', views.GetPerson.as_view(), name='get_person'),
    path('review/<slug:slug>/', views.AddReview.as_view(), name='review'),
]