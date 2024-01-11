from django.urls import path
from .views import movies_list, add_movie, edit_movie, delete_movie, category_list

urlpatterns = [
    path('movies/', movies_list, name='movies_list'),
    path('cat/', category_list, name='category_list'),
    path('movies/add/', add_movie, name='add_movie'),
    path('movies/edit/<int:movie_id>/', edit_movie, name='edit_movie'),
    path('movies/delete/<int:movie_id>/', delete_movie, name='delete_movie'),
]
