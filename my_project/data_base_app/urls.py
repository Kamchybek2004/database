from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_list, name='book_list'),
    path('', views.get_weather_data, name='book_list'),
    path('book/new/', views.book_create, name='book_create'),
    path('book/edit/<int:pk>/', views.book_edit, name='book_edit'),
    path('book/delete/<int:pk>/', views.book_delete, name='book_delete'),
]