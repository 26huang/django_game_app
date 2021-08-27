from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from ..gameplay.models import Game

#user needs to be loged in to visit this page
@login_required
def home(request):
    all_my_games = Game.objects.games_for_user(request.user)
    my_active_games = all_my_games.active()
    my_draw_games = all_my_games.draw()
    return render(request=request,
                  template_name='player/home.html',
                  context={'my_games': all_my_games,
                           'my_ngames': all_my_games.count(),
                           'my_active_games': my_active_games.count(),
                           'my_draw_games': my_draw_games.count(),
                           }
                  )