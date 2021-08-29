from django.urls import path
from . import views
from django.conf.urls import url
from django.contrib.auth.views import LoginView, LogoutView

app_name = 'player'

urlpatterns = [
    path('', views.home, name='home'),
    path('login/',
         LoginView.as_view(template_name='player/login_form.html'),
         name='player_login'),
    path('logout/',
         LogoutView.as_view(),
         name='player_logout'),
    # url(r'^$', views.home, name='home'),
]
