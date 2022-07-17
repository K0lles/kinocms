from django.urls import path
from . import views

urlpatterns = [
    path('cinema/', views.create_cinema, name='cinema'),
]
