from rest_framework import serializers
from .models import Favorite
from books.models import Book
from books.serializers import BookSerializer

class FavoriteSerializer(serializers.ModelSerializer):
    book = BookSerializer(read_only=True)
    book_id = serializers.PrimaryKeyRelatedField(
        queryset=Book.objects.all(),
        source='book',
        write_only=True
    )

    class Meta:
        model = Favorite
        fields = ['id', 'book', 'book_id', 'added_at']
