from django.urls import path
from . import views

urlpatterns = [
    path('banner/', views.create_banner, name='create_banner'),
    path('cinema/', views.cinema_view, name='cinema'),
    path('cinema/create/', views.create_cinema, name='cinema_create'),
    path('cinema/update/<int:pk>/', views.update_cinema, name='update_cinema'),
    path('hall/<int:cinema_pk>/create/', views.create_hall, name='create_hall'),
    path('hall/update/<int:hall_pk>/', views.update_hall, name='update_hall'),
    path('page/create/', views.create_page, name='page_create')
]
