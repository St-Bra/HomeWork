from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=255)
    biography = models.TextField(blank=True)
    birth_year = models.IntegerField(null=True, blank=True)

class Genre(models.Model):
    name = models.CharField(max_length=100)

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    description = models.TextField()
    published_year = models.IntegerField()
    isbn = models.CharField(max_length=13, blank=True)
    genre = models.ForeignKey(Genre, on_delete=models.SET_NULL, null=True)
    available = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.title
