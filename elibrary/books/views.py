from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Book, Author, Genre
from .serializers import BookSerializer, AuthorSerializer, GenreSerializer


# ========== КНИГИ ==========

class BookListCreateView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request):
        books = Book.objects.filter(is_deleted=False)
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BookDetailView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request, pk):
        try:
            book = Book.objects.get(pk=pk, is_deleted=False)
        except Book.DoesNotExist:
            return Response({'detail': 'Not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = BookSerializer(book)
        return Response(serializer.data)

    def delete(self, request, pk):
        try:
            book = Book.objects.get(pk=pk, is_deleted=False)
        except Book.DoesNotExist:
            return Response({'detail': 'Not found'}, status=status.HTTP_404_NOT_FOUND)
        book.is_deleted = True
        book.save()
        return Response({'detail': 'Book soft-deleted'}, status=status.HTTP_204_NO_CONTENT)


# ========== АВТОРЫ ==========

class AuthorListCreateView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request):
        authors = Author.objects.all()
        serializer = AuthorSerializer(authors, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AuthorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AuthorDetailView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request, pk):
        try:
            author = Author.objects.get(pk=pk)
        except Author.DoesNotExist:
            return Response({'detail': 'Not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = AuthorSerializer(author)
        return Response(serializer.data)


# ========== ЖАНРЫ ==========

class GenreListCreateView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request):
        genres = Genre.objects.all()
        serializer = GenreSerializer(genres, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = GenreSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GenreDetailView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request, pk):
        try:
            genre = Genre.objects.get(pk=pk)
        except Genre.DoesNotExist:
            return Response({'detail': 'Not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = GenreSerializer(genre)
        return Response(serializer.data)
