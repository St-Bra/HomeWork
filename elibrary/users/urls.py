
from django.urls import path
from .views import FavoriteView

urlpatterns = [
    path('favorites/', FavoriteView.as_view(), name='favorite-list'),  # GET и POST запросы
    path('favorites/<int:pk>/', FavoriteView.as_view(), name='favorite-delete'),  # DELETE запрос
]
