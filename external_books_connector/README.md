# external_books_connector

Django-приложение для поиска книг по названию через API [OpenLibrary.org](https://openlibrary.org).

## Установка

```bash
git clone https://github.com/yourusername/external_books_connector.git

Скопируй директорию external_books в свой Django-проект и подключи:
# settings.py
INSTALLED_APPS = [
    ...
    'external_books',
]


Подключи маршруты:
# urls.py

path('external-books/', include('external_books.urls')),


Открой в браузере:
http://localhost:8000/external-books/search/