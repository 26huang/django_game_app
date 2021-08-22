from django.urls import path
from . import views
from django.conf.urls import url

app_name = 'player'

urlpatterns = [
    path('', views.welcome, name='welcome'),
    # url(r'^$', views.home, name='home'),
]
