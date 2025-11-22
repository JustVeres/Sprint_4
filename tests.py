import pytest
from main import BooksCollector

class TestBooksCollector:

    # Позитивные проверки метода add_new_book (добавление книги в словарь без жанра):
    def test_add_new_book_add_one_book_added_one_book(self, collector): # Проверка добавления одной новой книги
        collector.add_new_book('Гарри-Шпроттер')
        assert len(collector.get_books_genre()) == 1 # ОР: добавлена одна книга

    def test_add_new_book_add_two_book_added_two_book(self, collector): # Проверка добавления двух новых книг
        collector.add_new_book('Пуля-Квант')
        collector.add_new_book('Зона поражения')
        assert len(collector.get_books_genre()) == 2 # ОР: добавлено две книги

    @pytest.mark.parametrize('letters_in', ['Г', 'ЭтаКнигаСостоитИзСорокаСимволовОнаХороша'])        # Проверка добавления одной книги
    def test_adds_new_book_in_boundary_values_added_one_book(self, collector, letters_in):    # с кол-вом символов [1, 40]
        collector.add_new_book(letters_in)
        assert len(collector.get_books_genre()) == 1 # ОР: добавлена одна книга

    def test_add_new_book_two_identical_books_added_one_book(self, collector): # Проверка добавления двух новых книг с одинаковым названием
        collector.add_new_book('Мгла')
        collector.add_new_book('Мгла')
        assert len(collector.get_books_genre()) == 1 # ОР: добавлена одна книга

    def test_add_new_book_add_book_without_genre_added_book_without_genre(self, collector): # Проверка, что была добавлена книга без жанра
        collector.add_new_book('Сомнамбула')
        assert list(collector.get_books_genre().values()) == [''] # ОР: добавлена книга без жанра(значения)

    # Негативные проверки метода add_new_book (добавление книги в словарь без жанра):
    @pytest.mark.parametrize('letters_out', ['', 'ЭтаКнигаСостоитИзСорокаОдногоСимволаОнаКл'])        # Проверка добавления одной книги
    def test_adds_new_book_out_boundary_values_not_added_book(self, collector, letters_out):   # с кол-вом символов [0, 41]
        collector.add_new_book(letters_out)
        assert len(collector.get_books_genre()) == 0 # ОР: книга отсутствует в списке добавленных книг

    # Позитивные проверки метода set_book_genre(устанавливаем книге жанр)
    def test_set_book_genre_add_book_name_and_genre_added_book_genre(self, collector): # Проверка добавления жанра добавленной книги
        collector.add_new_book('Звёздный путь')
        collector.set_book_genre('Звёздный путь', 'Фантастика')
        assert collector.get_book_genre('Звёздный путь') == 'Фантастика' # ОР: добавлен жанр книги

    # Негативные проверки метода set_book_genre(устанавливаем книге жанр)
    def test_set_book_genre_add_book_without_add_new_book_not_added(self, collector): # Проверка добавления книги с жанром,
        collector.set_book_genre('Прятки', 'Детективы')                                      # если не добавили название книги в books_genre
        assert len(collector.get_books_genre()) == 0 # ОР: жанр книги не добавлен

    def test_set_book_genre_add_book_without_genre_not_added_genre(self, collector): # Проверка добавления книги
        collector.add_new_book('ЕГЭ-2026')                                                  # с несуществующим жанром
        collector.set_book_genre('ЕГЭ-2026', 'Обучающие')
        assert list(collector.get_books_genre().values()) == [''] # ОР: жанр книги не добавлен

    def test_set_book_genre_add_genre_without_name_genre_not_added(self, collector): # Проверка добавления книги с жанром без имени книги
        collector.add_new_book('Волшебник Изумрудного города')
        collector.set_book_genre('', 'Мультфильмы')
        assert list(collector.get_books_genre().values()) == [''] # ОР: жанр книги не добавлен

    def test_set_book_genre_add_without_genre_not_added_genre(self, collector): # Проверка установки жанра с пустым жанром
        collector.add_new_book('Перекресток Воронов')
        collector.set_book_genre('Перекресток Воронов', '')
        assert list(collector.get_books_genre().values()) == [''] # ОР: жанр книги не добавлен

    # Проверки метода get_book_genre(получаем жанр книги по её имени)
    def test_get_books_genre_empty_initial_state(self, collector): # Проверка пустого словаря при инициализации
        assert len(collector.get_books_genre()) == 0 # ОР: возвращается пустой словарь

    def test_get_book_genre_add_book_with_genre_get_genre(self, collector): # Проверка получения жанра по имени
        collector.add_new_book('Во тьме')
        collector.set_book_genre('Во тьме', 'Ужасы')
        assert collector.get_book_genre('Во тьме') == 'Ужасы' # ОР: получен жанр соответсвующий названию книги

    # Проверки метода get_books_with_specific_genre(выводим список книг с определённым жанром)
    # позитивные проверки get_books_with_specific_genre:
    @pytest.mark.parametrize('genre_name', BooksCollector().genre)
    def test_get_books_with_specific_genre_add_name_and_genre_derivation(self, collector, genre_name): # Проверка вывода книг по каждому жанру
        book_name = 'Универсальная книга'
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre_name)
        assert collector.get_books_with_specific_genre(genre_name) == [book_name] # ОР: название книги выводится по текущему жанру

    # негативные проверки get_books_with_specific_genre:
    def test_get_books_with_specific_genre_nonexistent_name_not_added(self, collector): # Проверка вывода книг с несуществующим жанром
        collector.add_new_book('Ониксовый шторм')
        collector.set_book_genre('Ониксовый шторм', 'Фантастика')
        assert collector.get_books_with_specific_genre('Несуществующий жанр') == [] # ОР: название книги не выводится по текущему несуществующему жанру

    def test_get_books_with_specific_genre_multiple_books_same_genre_added_three_books(self, collector): # Проверка вывода нескольких книг
        books = ['Книга1', 'Книга2', 'Книга3']                                                           # с определённым жанром
        for book in books:
            collector.add_new_book(book)
            collector.set_book_genre(book, 'Комедии')
        book_result = collector.get_books_with_specific_genre('Комедии')
        assert len(book_result) == 3 # ОР: выводятся 3 книги с определённым жанром

    # Проверки метода get_books_genre(выводит текущий словарь books_genre)
    def test_add_new_book_name_value_valid_name_book(self, collector): # Проверка вывода словаря с книгами
        name_book = 'Лунь'
        collector.add_new_book(name_book)
        assert collector.get_books_genre() == {name_book: ''} # ОР: выводится текущий словарь с названием книги

    # Проверки метода get_books_for_children(возвращает книги, которые подходят детям. У жанра книги не должно быть возрастного рейтинга)
    # Позитивные проверки get_books_for_children
    def test_get_books_for_children_with_allowed_genres(self, collector):  # Проверяем, что все книги с подходящими жанрами возвращаются
        test_books = [
            ('Книга1', 'Фантастика'),
            ('Книга2', 'Мультфильмы'),
            ('Книга3', 'Комедии')]

        for book_name, genre in test_books:
            collector.add_new_book(book_name)
            collector.set_book_genre(book_name, genre)

        result = collector.get_books_for_children()
        expected_books = ['Книга1', 'Книга2', 'Книга3']

        assert len(result) == len(expected_books) and set(result) == set(expected_books) # ОР: добавлено 3 книги с подходящими жанрами для детей

    def test_get_books_for_children_excludes_age_rated_genres(self, collector): # Проверяем, что книги с возрастным рейтингом не возвращаются
        test_books = [
            ('Страшная книга', 'Ужасы'),
            ('Детективная история', 'Детективы')]

        for book_name, genre in test_books:
            collector.add_new_book(book_name)
            collector.set_book_genre(book_name, genre)

        result = collector.get_books_for_children()
        assert result == [] # ОР: книги с возрастным рейтингом не для детей не добавлены

    def test_get_books_for_children_mixed_genres(self, collector): # Проверяем, что возвращены только подходящие книги, если добавлены все жанры
        test_books = [
            ('Детская книга', 'Мультфильмы'),  # подходит
            ('Страшная книга', 'Ужасы'),       # не подходит
            ('Фантастическая', 'Фантастика'),  # подходит
            ('Детектив', 'Детективы'),         # не подходит
            ('Комедийная', 'Комедии')]         # подходит

        for book_name, genre in test_books:
            collector.add_new_book(book_name)
            collector.set_book_genre(book_name, genre)

        result = collector.get_books_for_children()
        expected_books = ['Детская книга', 'Фантастическая', 'Комедийная']
        assert len(collector.get_books_for_children()) == len(expected_books) and set(result) == set(expected_books) # ОР: добавлено 3 книги с подходящими жанрами для детей

    # Негативные проверки get_books_for_children
    def test_get_books_for_children_without_genre(self, collector): # Проверяем, что книга без жанра не должна возвращаться
        collector.add_new_book('Книга без жанра')
        assert collector.get_books_for_children() == [] # ОР: книги без установленного жанра не возвращаются

    def test_get_books_for_children_with_invalid_genre(self, collector): # Проверяем, что книга с невалидным жанром не должна возвращаться
        collector.add_new_book('Книга с невалидным жанром')
        collector.books_genre['Книга с невалидным жанром'] = 'Несуществующий жанр'
        assert collector.get_books_for_children() == [] # ОР: книги с невалидным жанром не возвращаются

    def test_get_books_for_children_empty_collection(self, collector): # Проверяем, что для пустой коллекции возвращается пустой список
        assert collector.get_books_for_children()== [] # ОР: возвращается пустой список

    # Проверки метода add_book_in_favorites(добавляет книгу в избранное. Книга должна находиться в словаре books_genre. Повторно добавить книгу в избранное нельзя)
    def test_add_book_in_favorites_success(self, collector): # Проверяем успешное добавление книги в избранное
        book_name = 'Книга для избранных'
        collector.add_new_book(book_name)
        collector.add_book_in_favorites(book_name)
        favorites = collector.get_list_of_favorites_books()
        assert book_name in favorites and len(favorites) == 1 # ОР: книга появилась в списке избранных

    def test_cannot_add_nonexistent_book_to_favorites(self, collector): # Проверяем, что нельзя добавить несуществующую книгу в избранное
        book_name = 'Несуществующая книга'
        collector.add_book_in_favorites(book_name)
        favorites = collector.get_list_of_favorites_books()
        assert book_name not in favorites and len(favorites) == 0 # ОР: книга не добавлена в избранное

    def test_cannot_add_duplicate_book_to_favorites(self, collector): # Проверяем, что нельзя добавить книгу в избранное дважды
        book_name = 'Книга для избранных'
        collector.add_new_book(book_name)
        collector.add_book_in_favorites(book_name) # Первое добавление
        favorites_first = collector.get_list_of_favorites_books()
        collector.add_book_in_favorites(book_name) # Второе добавление
        favorites_second = collector.get_list_of_favorites_books()
        assert book_name in favorites_second and len(favorites_second) == 1 and favorites_first == favorites_second # ОР: книга не добавилась повторно

    # Проверки метода delete_book_from_favorites(удаляет книгу из избранного, если она там есть)
    def test_delete_book_from_favorites_success(self, collector): # Проверяем успешное удаление книги из избранного
        book_name = 'Книга удаляется из избранного'
        collector.add_new_book(book_name)
        collector.add_book_in_favorites(book_name)
        collector.delete_book_from_favorites(book_name)
        favorites = collector.get_list_of_favorites_books()
        assert book_name not in favorites and len(favorites) == 0 # ОР: добавленная книга удалена из избранного

    def test_delete_nonexistent_book_from_favorites(self, collector): # Проверяем удаление несуществующей книги из избранного
        book_name = 'Несуществующая книга'
        collector.delete_book_from_favorites(book_name)
        favorites = collector.get_list_of_favorites_books()
        assert book_name not in favorites and len(favorites) == 0 # ОР: список избранного остался пустым

    def test_delete_book_not_in_favorites(self, collector): # Проверка удаления книги, которая есть в коллекции, но не в избранном
        book_name = 'Книга в коллекции'
        collector.add_new_book(book_name)
        collector.delete_book_from_favorites(book_name)
        favorites = collector.get_list_of_favorites_books()
        assert book_name not in favorites and len(favorites) == 0 # ОР: список избранного остался пустым

    # Проверки метода get_list_of_favorites_books(получает список избранных книг)
    def test_get_list_of_favorites_books_empty(self, collector): # Проверка пустого списка, когда нет избранных книг
        assert collector.get_list_of_favorites_books() == [] # ОР: список избранного пустой

    def test_get_list_of_favorites_books_with_one_book(self, collector): # Проверка списка с одной книгой, когда добавлена одна книга
        book_name = '1984'
        collector.add_new_book(book_name)
        collector.add_book_in_favorites(book_name)
        assert collector.get_list_of_favorites_books() == [book_name] # ОР: добавлена книга с названием
