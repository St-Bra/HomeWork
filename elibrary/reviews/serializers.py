from rest_framework import serializers
from .models import Review
from django.contrib.auth.models import User
from books.models import Book

class ReviewSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    book = serializers.StringRelatedField()

    class Meta:
        model = Review
        fields = '__all__'
