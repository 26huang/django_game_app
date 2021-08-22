from django.shortcuts import render


def welcome(request):
    return render(request=request, template_name='player/home.html')