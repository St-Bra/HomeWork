from rest_framework import serializers
from .models import Favorite
from books.models import Book
from books.serializers import BookSerializer

class FavoriteSerializer(serializers.ModelSerializer):
    # Поле для передачи только ID книги
    book = BookSerializer(read_only=True)
    book_id = serializers.PrimaryKeyRelatedField(
        queryset=Book.objects.all(),
        source='book',
        write_only=True  # Это поле нужно только для записи, его не нужно показывать в ответе
    )

    class Meta:
        model = Favorite
        fields = ['id', 'book', 'book_id', 'added_at']
