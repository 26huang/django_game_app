from django.shortcuts import render
from ..gameplay.models import Game


def welcome(request):
    return render(request=request,
                  template_name='player/home.html',
                  context={'ngames': Game.objects.count()})