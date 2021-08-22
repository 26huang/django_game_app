from django.urls import path
from . import views
from django.conf.urls import url

app_name = 'gameplay'

urlpatterns = [
    path('', views, name='gameplay'),
]
