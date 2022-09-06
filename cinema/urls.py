from django.urls import path
from . import views
urlpatterns = [
    path('home/', views.home_view, name='home'),
    path('poster/', views.poster_view, name='poster'),
]
