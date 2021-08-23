from django.shortcuts import render
from ..gameplay.models import Game


def home(request):
    all_games = Game.objects.all()
    all_my_games = Game.objects.games_for_user(request.user)
    my_active_games = all_my_games.active()
    active_games = all_games.active()
    my_draw_games = all_my_games.draw()
    draw_games = all_games.draw()

    return render(request,
                  template_name='main/home.html',
                  context={
                      'games': all_games,
                      'ngames': all_games.count(),
                      'active_games': active_games.count(),
                      'draw_games': draw_games.count(),

                      'my_games': all_my_games,
                      'my_ngames': all_my_games.count(),
                      'my_active_games': my_active_games.count(),
                      'my_draw_games': my_draw_games.count()
                  }
    )