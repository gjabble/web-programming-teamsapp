from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('api/teams', views.teams, name='teams'),
    path('api/players', views.players, name='players'),
    path('api/players/<int:playerid>', views.player, name='player'),
    path('api/teams/<int:teamid>', views.team, name='team')
]