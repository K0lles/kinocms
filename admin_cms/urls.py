from django.urls import path
from . import views

urlpatterns = [
    path('main/', views.CinemaCreateView.as_view(), name='main'),
]
