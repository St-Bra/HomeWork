from django.urls import path
from .views import ReviewListCreateView, ReviewDetailView

urlpatterns = [
    # Список отзывов и создание нового
    path('reviews/', ReviewListCreateView.as_view(), name='review-list-create'),

    # Детали отзыва по ID и удаление
    path('reviews/<int:pk>/', ReviewDetailView.as_view(), name='review-detail'),
]
