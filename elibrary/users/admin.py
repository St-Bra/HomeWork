from django.contrib import admin
from .models import Favorite

@admin.register(Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    list_display = ('user', 'book', 'added_at')
    list_filter = ('user',)
    search_fields = ('user__username', 'book__title')