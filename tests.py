import pytest
from main import BooksCollector

class TestBooksCollector:

    # Проверка добавления двух книг в словарь books_genre (начальный пример)
    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.get_books_genre()) == 2        
                            

    # Проверка добавления трех книг в словарь books_genre (именно мой тест, а не тот, который уже тут был)
    def test_add_new_book_add_three_books(self):
        collector = BooksCollector()

        collector.add_new_book('Маленький принц')
        collector.add_new_book('Тревожные люди')
        collector.add_new_book('Алиса в стране Чудес')

        assert len(collector.get_books_genre()) == 3


    # Негативная проверка добавления книги с пустым названием и с длинным названием (больше 40 символов)
    @pytest.mark.parametrize('name', [
        '',
        'Бабушка велела кланяться и передать что просит прощения очень очень очень',
    ])
    def test_add_new_book_not_add_book_with_invalid_name(self, name):
        collector = BooksCollector()

        collector.add_new_book(name)

        assert len(collector.get_books_genre()) == 0


    # Проверка установления жанра, если книга есть в словаре books_genre
    def test_set_book_genre_set_valid_genre(self):
        collector = BooksCollector()

        collector.add_new_book('Гарри Поттер')
        collector.set_book_genre('Гарри Поттер', 'Фантастика')

        assert collector.get_book_genre('Гарри Поттер') == 'Фантастика'


    # Проверка, что метод get_book_genre возвращает жанр книги по ее названию
    def test_get_book_genre_return_correct_genre(self):
        collector = BooksCollector()

        collector.add_new_book('Дюплекс')
        collector.set_book_genre('Дюплекс', 'Комедии')

        assert collector.get_book_genre('Дюплекс') == 'Комедии'


     # Проверка вывода книги с определенным жанром
    @pytest.mark.parametrize(
        'genre, expected',
        [
            ('Фантастика', ['Русалочка']),
            ('Детективы', ['Золушка']),
        ]
    )
    def test_get_books_with_specific_genre_return_books(self, genre, expected):
        collector = BooksCollector()

        collector.add_new_book('Русалочка')
        collector.add_new_book('Золушка')

        collector.set_book_genre('Русалочка', 'Фантастика')
        collector.set_book_genre('Золушка', 'Детективы')

        assert collector.get_books_with_specific_genre(genre) == expected


    # Проверка, что метод get_books_genre выводит текущий словарь books_genre
    def test_get_books_genre_return_dictionary(self):
        collector = BooksCollector()

        collector.add_new_book('Властелин колец')
        collector.set_book_genre('Властелин колец', 'Фантастика')

        assert collector.get_books_genre() == {'Властелин колец': 'Фантастика'}


    # Проверка, что метод get_books_for_children возвращает книги, которые подходят детям
    def test_get_books_for_children_return_books_without_age_rating(self):
        collector = BooksCollector()

        collector.add_new_book('Тайна третьей планеты')
        collector.add_new_book('Крик')

        collector.set_book_genre('Тайна третьей планеты', 'Фантастика')
        collector.set_book_genre('Крик', 'Ужасы')

        assert collector.get_books_for_children() == ['Тайна третьей планеты']


    # Проверка, что метод add_book_in_favorites добавляет книгу в избранное
    def test_add_book_in_favorites_add_book(self):
        collector = BooksCollector()
        collector.add_new_book('Шантарам')
        collector.add_book_in_favorites('Шантарам')

        assert collector.get_list_of_favorites_books() == ['Шантарам']


    # Проверка, что метод delete_book_from_favorites удаляет книгу из избранного
    def test_delete_book_from_favorites_remove_book(self):
        collector = BooksCollector()
        collector.add_new_book('Гранатовый браслет')
        collector.add_book_in_favorites('Гранатовый браслет')
        collector.delete_book_from_favorites('Гранатовый браслет')

        assert collector.get_list_of_favorites_books() == []


    # Проверка, что метод get_list_of_favorites_books получает список избранных книг
    def test_get_list_of_favorites_books_return_list(self):
        collector = BooksCollector()
        collector.add_new_book('Сумерки')
        collector.add_new_book('Алые паруса')
        collector.add_book_in_favorites('Сумерки')
        collector.add_book_in_favorites('Алые паруса')

        assert collector.get_list_of_favorites_books() == ['Сумерки', 'Алые паруса']     




        