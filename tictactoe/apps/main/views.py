from django.shortcuts import render, redirect
from ..gameplay.models import Game


def welcome(request):
    if request.user.is_authenticated:
        return redirect('player:home')
    else:
        all_games = Game.objects.all()
        active_games = all_games.active()
        draw_games = all_games.draw()
        return render(request,
                      template_name='main/welcome.html',
                      context={
                          'games': all_games,
                          'ngames': all_games.count(),
                          'active_games': active_games.count(),
                          'draw_games': draw_games.count(),
                      }
    )