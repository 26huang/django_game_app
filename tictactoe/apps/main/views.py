from django.shortcuts import render


def home(request):
    return render(request, template_name='main/home.html')