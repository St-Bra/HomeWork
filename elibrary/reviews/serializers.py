from rest_framework import serializers
from .models import Review
from books.models import Book
from django.contrib.auth.models import User

class ReviewSerializer(serializers.ModelSerializer):
    # Поле book будет представлять собой только ID книги
    book = serializers.PrimaryKeyRelatedField(queryset=Book.objects.all())
    user = serializers.StringRelatedField(read_only=True)  # Ссылка на текущего пользователя

    class Meta:
        model = Review
        fields = ['id', 'book', 'user', 'rating', 'text', 'created_at']
