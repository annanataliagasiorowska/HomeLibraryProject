import data_manager
from psycopg2 import sql


def get_books_all():
    return data_manager.execute_select('SELECT title FROM book;')


def post_book(book_details):
    data_manager.execute_dml_statement("""INSERT INTO book (title, release_year) VALUES (%(title)s)""",
                                       {'title': book_details['title']})


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


