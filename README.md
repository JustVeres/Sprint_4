# qa_python
## 28 когорта

### Выполенные проверки в файле tests.py:
#### add_new_book:
1. [X] **test_add_new_book_add_one_book_added_one_book** — Проверка добавления одной новой книги.
2. [X] **test_add_new_book_add_two_book_added_two_book** — Проверка добавления двух новых книг.
3. [X] **test_adds_new_book_in_boundary_values_added_one_book** — Проверка добавления одной книги с кол-вом символов [1, 40]
4. [X] **test_add_new_book_two_identical_books_added_one_book** — Проверка добавления двух новых книг с одинаковым названием.
5. [X] **test_add_new_book_add_book_without_genre_added_book_without_genre** — Проверка, что была добавлена книга без жанра.
6. [X] **test_adds_new_book_out_boundary_values_not_added_book** — Проверка добавления одной книги с кол-вом символов [0, 41]
   
#### set_book_genre:
1. [X] **test_set_book_genre_add_book_name_and_genre_added_book_genre** — Проверка добавления жанра добавленной книги.
2. [X] **test_set_book_genre_add_book_without_add_new_book_not_added** — Проверка добавления книги с жанром, если не добавили название книги в books_genre.
3. [X] **test_set_book_genre_add_book_without_genre_not_added_genre** — Проверка добавления книги с несуществующим жанром.
4. [X] **test_set_book_genre_add_genre_without_name_genre_not_added** — Проверка добавления книги с жанром без имени книги.
5. [X] **test_set_book_genre_add_without_genre_not_added_genre** — Проверка установки жанра с пустым жанром.

#### get_book_genre:
1. [X] **test_get_book_genre_add_book_with_genre_get_genre** — Проверка получения жанра по имени.
2. [X] **test_get_book_genre_existing_book_without_genre** — Проверка получения пустой строки для книги без установленного жанра.
3. [X] **test_get_book_genre_nonexistent_book** — Проверка получения жанра по имени несуществующей книги.
4. [X] **test_get_book_genre_empty_string_book_name** — Проверка получения жанра по имени пустого названия книги.

#### get_books_with_specific_genre:
1. [X] **test_get_books_with_specific_genre_add_name_and_genre_derivation** — Проверка вывода книг по каждому жанру.
2. [X] **test_get_books_with_specific_genre_nonexistent_name_not_added** — Проверка вывода книг с несуществующим жанром.
3. [X] **test_get_books_with_specific_genre_multiple_books_same_genre_added_three_books** — Проверка вывода нескольких книг с определённым жанром.

#### get_books_genre:
1. [X] **test_add_new_book_name_value_valid_name_book** — Проверка вывода словаря с книгами.
2. [X] **** —
#### get_books_for_children:
1. [X] **test_get_books_for_children_with_allowed_genres** — Проверяем, что все книги с подходящими жанрами возвращаются.
2. [X] **test_get_books_for_children_excludes_age_rated_genres** — Проверяем, что книги с возрастным рейтингом не возвращаются.
3. [X] **test_get_books_for_children_mixed_genres** — Проверяем, что возвращены только подходящие книги, если добавлены все жанры.
4. [X] **test_get_books_for_children_without_genre** — Проверяем, что книга без жанра не должна возвращаться.
5. [X] **test_get_books_for_children_with_invalid_genre** — Проверяем, что книга с невалидным жанром не должна возвращаться.
6. [X] **test_get_books_for_children_empty_collection** — Проверяем, что для пустой коллекции возвращается пустой список.

#### add_book_in_favorites:
1. [X] **test_add_book_in_favorites_success** — Проверяем успешное добавление книги в избранное.
2. [X] **test_cannot_add_nonexistent_book_to_favorites** — Проверяем, что нельзя добавить несуществующую книгу в избранное.
3. [X] **test_cannot_add_duplicate_book_to_favorites** — Проверяем, что нельзя добавить книгу в избранное дважды.

#### delete_book_from_favorites:
1. [X] **test_delete_book_from_favorites_success** — Проверяем успешное удаление книги из избранного.
2. [X] **test_delete_nonexistent_book_from_favorites** — Проверяем удаление несуществующей книги из избранного.
3. [X] **test_delete_book_not_in_favorites** — Проверка удаления книги, которая есть в коллекции, но не в избранном.

#### get_list_of_favorites_books:
1. [X] **test_get_list_of_favorites_books_empty** — Проверка пустого списка, когда нет избранных книг.
2. [X] **test_get_list_of_favorites_books_with_one_book** — Проверка списка с одной книгой, когда добавлена одна книга. 