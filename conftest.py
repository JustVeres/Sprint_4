import pytest
from main import BooksCollector

@pytest.fixture # Фикстура для инициализации класса BooksCollector
def collector():
    collector = BooksCollector()
    return collector

@pytest.fixture # Фикстура для вывода списка книг метода get_books_genre
def books(collector):
    books = collector.get_books_genre()
    return books