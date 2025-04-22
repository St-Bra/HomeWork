from django.shortcuts import render
from .api import search_books_by_title

def book_search_view(request):
    query = request.GET.get('q', '')
    books = search_books_by_title(query) if query else []
    return render(request, 'external_books/book_list.html', {'books': books, 'query': query})
