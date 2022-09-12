from django.urls import path
from . import views

urlpatterns = [
    path('<int:movie_pk>/', views.movie_detail, name='movie_detail'),
    path('schedule/', views.schedule_view, name='schedule'),
]
