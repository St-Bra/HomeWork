from django.urls import path
from .views import (
    BookListCreateView, BookDetailView,
    AuthorListCreateView, AuthorDetailView,
    GenreListCreateView, GenreDetailView
)

urlpatterns = [
    path('', BookListCreateView.as_view(), name='home-page'),
    # Книги
    path('books/', BookListCreateView.as_view(), name='book-list-create'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),

    # Авторы
    path('authors/', AuthorListCreateView.as_view(), name='author-list-create'),
    path('authors/<int:pk>/', AuthorDetailView.as_view(), name='author-detail'),

    # Жанры
    path('genres/', GenreListCreateView.as_view(), name='genre-list-create'),
    path('genres/<int:pk>/', GenreDetailView.as_view(), name='genre-detail'),
]
