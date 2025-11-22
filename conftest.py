import pytest
from main import BooksCollector

@pytest.fixture # Фикстура для инициализации класса BooksCollector
def collector():
    collector = BooksCollector()
    return collector
