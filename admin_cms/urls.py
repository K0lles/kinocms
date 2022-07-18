from django.urls import path
from . import views

urlpatterns = [
    path('cinema/create/', views.create_cinema, name='cinema_create'),
    path('cinema/', views.cinema_view, name='cinema'),
]
