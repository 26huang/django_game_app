from django.shortcuts import render
from ..gameplay.models import Game


def home(request):
    # games_first_player = Game.objects.filter(
    #     first_player=request.user,
    #     status='F'
    # )
    # games_second_player = Game.objects.filter(
    #     second_player=request.user,
    #     status='S'
    # )
    #
    # all_my_games = list(games_first_player) + list(games_second_player)

    all_my_games = Game.objects.games_for_user(request.user)
    active_games = all_my_games.active()
    return render(request,
                  template_name='main/home.html',
                  context={'games': all_my_games, 'ngames': Game.objects.count()}
    )