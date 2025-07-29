from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # добавьте другие URL по необходимости
]