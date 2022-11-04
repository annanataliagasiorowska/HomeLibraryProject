import data_manager
from psycopg2 import sql


def get_books_all():
    return data_manager.execute_select('SELECT title FROM book;')


def post_book(book_details):
    data_manager.execute_dml_statement("""
    INSERT INTO book (title, user_id, genre_id, position, author_id, release_year) 
    VALUES (%(title)s, %(user_id)s, %(genre_id)s, %(position)s, %(author_id)s, %(release_year)s)""",
                                       {'title': book_details['title'],
                                        'user_id': book_details['user_id'],
                                        'genre_id': book_details['genre_id'],
                                        'position': book_details['position'],
                                        'author_id': book_details['author_id'],
                                        'release_year': book_details['release_year']})


# TODO: to add case insensitive search
def find_author_id(author_first_name, author_last_name):
    return data_manager.execute_select("""
    SELECT id FROM author 
    WHERE first_name = %(author_first_name)s 
    AND last_name = %(author_last_name)s""",
                                       {'author_first_name': author_first_name,
                                        'author_last_name': author_last_name}, False)


def find_user_id(owner):
    return data_manager.execute_select("""
    SELECT id FROM user
    WHERE name = %(owner)s""", {'owner': owner}, False)


def find_genre_id(genre):
    return data_manager.execute_select("""
    SELECT id FROM genre
    WHERE name = %(genre)s""", {'genre': genre}, False)


def get_genres():
    return data_manager.execute_select('SELECT name FROM genre;')


