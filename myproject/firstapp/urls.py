from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [

    path('', views.index, name='home'),
    path('game_1/', views.game_1, name='game_1'),
    path('game_2/', views.game_2, name='game_2'),
    path('game_3/', views.game_3, name='game_3'),
    path('about_me/', views.about_me, name='about_me'),
    path('static_game/', views.static_game, name='static_game'),
    path('full_name/', views.full_name, name='full_name')

]