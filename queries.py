import data_manager
from psycopg2 import sql


def get_books_all(offset, limit):
    return data_manager.execute_select("""
    SELECT b.title, b.release_year, b.rating, b.internal_rating, 
    CONCAT(a.first_name, ' ' , a.last_name) as Author 
    FROM book AS b
    LEFT OUTER JOIN author a on a.id = b.author_id
    LIMIT %(limit)s OFFSET %(offset)s;
    """, {'limit': limit, 'offset': offset, })


def count_books():
    return data_manager.execute_select('SELECT COUNT(id) FROM book')


def count_authors():
    return data_manager.execute_select('SELECT COUNT(id) FROM author')

# def count_records(database_table):
#     return data_manager.execute_select("""SELECT COUNT(id)
#     FROM %(database_table)s""", {'database_table': database_table})


def post_book(book_details):
    print("Book details: " + str(book_details))
    data_manager.execute_dml_statement("""
    INSERT INTO book (title, user_id, genre_id, "position", author_id, release_year) 
    VALUES (%(title)s, %(user_id)s, %(genre_id)s, %(position)s, %(author_id)s, %(release_year)s)""",
                                       {'title': book_details['title'],
                                        'user_id': book_details['user_id'],
                                        'genre_id': book_details['genre_id'],
                                        'position': book_details['position'],
                                        'author_id': book_details['author_id'],
                                        'release_year': book_details['release_year']})


def post_author(author_details):
    return data_manager.execute_dml_statement("""
    INSERT INTO author (first_name, last_name, birth_year, origin) 
    VALUES (%(first_name)s, %(last_name)s, %(birth_year)s, %(origin)s)
    RETURNING id""",
                                       {'first_name': author_details['first_name'],
                                        'last_name': author_details['last_name'],
                                        'birth_year': author_details['date_of_birth'],
                                        'origin': author_details['origin']})


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
    SELECT id FROM public.user
    WHERE name = %(owner)s""", {'owner': owner}, False)


def find_genre_id(genre):
    return data_manager.execute_select("""
    SELECT id FROM public.genre
    WHERE name = %(genre)s""", {'genre': genre}, False)


def get_genres():
    return data_manager.execute_select('SELECT name FROM genre;')


def get_last_author_id():
    return data_manager.execute_select('SELECT MAX(id) FROM public.author;', False)


def get_authors_all(offset, limit):
    return data_manager.execute_select("""
       SELECT CONCAT(first_name, ' ' , last_name) as Author, 
       TO_CHAR( birth_year:: DATE, 'dd.mm.yyyy') AS birthday, origin
       FROM author 
       ORDER BY last_name ASC
       LIMIT %(limit)s OFFSET %(offset)s;
       """, {'limit': limit, 'offset': offset, })



