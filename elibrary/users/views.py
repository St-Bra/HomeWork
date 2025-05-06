from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .models import Favorite
from .serializers import FavoriteSerializer
from books.models import Book


class FavoriteView(APIView):
    permission_classes = [IsAuthenticated]

    # Получение списка избранных книг
    def get(self, request):
        favorites = Favorite.objects.filter(user=request.user)
        serializer = FavoriteSerializer(favorites, many=True)
        return Response(serializer.data)

    # Добавление книги в избранное
    def post(self, request):
        book_id = request.data.get('book_id')

        if not book_id:
            return Response({"detail": "Book ID is required."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            book = Book.objects.get(id=book_id)
        except Book.DoesNotExist:
            return Response({"detail": "Book not found."}, status=status.HTTP_404_NOT_FOUND)

        if Favorite.objects.filter(user=request.user, book=book).exists():
            return Response({"detail": "Book is already in favorites."}, status=status.HTTP_400_BAD_REQUEST)

        favorite = Favorite.objects.create(user=request.user, book=book)
        serializer = FavoriteSerializer(favorite)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    # Удаление книги из избранного
    def delete(self, request, pk):
        try:
            favorite = Favorite.objects.get(id=pk, user=request.user)
        except Favorite.DoesNotExist:
            return Response({"detail": "Favorite not found."}, status=status.HTTP_404_NOT_FOUND)

        favorite.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
