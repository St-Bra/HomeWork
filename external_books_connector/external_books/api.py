import requests

def search_books_by_title(title):
    url = f"https://openlibrary.org/search.json?title={title}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json().get('docs', [])
    return []
