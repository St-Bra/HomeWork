from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Review
from .serializers import ReviewSerializer


class ReviewListCreateView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request):
        reviews = Review.objects.all()
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)  # Устанавливаем пользователя как текущего
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ReviewDetailView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request, pk):
        try:
            review = Review.objects.get(pk=pk, is_deleted=False)
        except Review.DoesNotExist:
            return Response({'detail': 'Review not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = ReviewSerializer(review)
        return Response(serializer.data)

    def delete(self, request, pk):
        try:
            review = Review.objects.get(pk=pk, is_deleted=False)
        except Review.DoesNotExist:
            return Response({'detail': 'Review not found'}, status=status.HTTP_404_NOT_FOUND)
        review.is_deleted = True
        review.save()
        return Response({'detail': 'Review soft-deleted'}, status=status.HTTP_204_NO_CONTENT)
