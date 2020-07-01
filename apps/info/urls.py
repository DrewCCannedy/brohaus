"""Urls for the Info app."""
from django.urls import path

from . import views

app_name = 'info'

urlpatterns = [
    path('', views.home, name='home'),
    path('points/', views.gecko_points, name="points")
]
