from flask import Flask, jsonify, render_template, request, redirect

import queries

app = Flask(__name__)
app.secret_key = 'ghbdtn93vbh65bdctv407yfv'


@app.route("/")
@app.route("/index")
def index():
    return render_template('index.html')


LIMIT = 10


@app.route('/api/books')
def api_books():
    page = int(request.args.get('page', 1))
    pages_all, offset = count_offset_books(page)
    return jsonify(queries.get_books_all(offset, LIMIT))


def count_offset_books(page):
    number_of_books = queries.count_books()[0]['count']
    pages_all = number_of_books // LIMIT + 1
    offset = (page - 1) * LIMIT
    return pages_all, offset


# def count_offset(page_number, database_table):
#     number_of_records = queries.count_records(database_table)[0]['count']
#     pages_all = number_of_records // LIMIT + 1
#     offset = (page_number - 1) * LIMIT
#     return pages_all, offset


@app.route("/books")
def books():
    page = int(request.args.get('page', 1))
    pages_all, offset = count_offset_books(page)
    return render_template('books.html', page=page, pages_all=pages_all)


def count_offset_authors(page):
    number_of_authors = queries.count_authors()[0]['count']
    pages_all = number_of_authors // LIMIT + 1
    offset = (page - 1) * LIMIT
    return pages_all, offset


@app.route('/api/authors')
def api_authors():
    page = int(request.args.get('page', 1))
    pages_all, offset = count_offset_authors(page)
    return jsonify(queries.get_authors_all(offset, LIMIT))


@app.route("/authors")
def authors():
    page = int(request.args.get('page', 1))
    pages_all, offset = count_offset_authors(page)
    return render_template('authors.html', page=page, pages_all=pages_all)


@app.route("/about")
def about():
    return render_template('about.html')


@app.route("/owners")
def owners():
    return render_template('owners.html')


@app.route("/borrowed")
def borrowed():
    return render_template('borrowed.html')


@app.route("/search")
def search():
    return render_template('search.html')


@app.route("/new_books", methods=["GET", "POST"])
# @login_required
def add_book():
    book_to_add = {}
    if request.method == "GET":
        genres = queries.get_genres()
        return render_template('new_books.html', genres=genres)
    else:
        book_to_add['title'] = request.form['title']
        owner = request.form['owner_name']
        user_id = queries.find_user_id(owner)
        book_to_add['user_id'] = user_id['id']
        genre = request.form['genre_name']
        print('Genre: ' + str(genre))
        genre_id = queries.find_genre_id(genre)
        print('Genre id: ' + str(genre_id))
        book_to_add['genre_id'] = genre_id['id']
        book_to_add['position'] = request.form['position_name']
        author_first_name = request.form['author_first']
        author_last_name = request.form['author_last']
        author_id = queries.find_author_id(author_first_name, author_last_name)
        book_to_add['release_year'] = request.form['release_year']
        if author_id:
            book_to_add['author_id'] = author_id['id']
        else:
            return render_template('new_authors.html', title=book_to_add['title'],
                                   user_id=book_to_add['user_id'],
                                   genre_id=book_to_add['genre_id'],
                                   position=book_to_add['position'],
                                   release_year=book_to_add['release_year'])
        queries.post_book(book_to_add)
        return redirect('/books')


@app.route("/new_authors", methods=["GET", "POST"])
# @login_required
def add_author():
    author_to_add = {}
    if request.method == "GET":
        return render_template('/new_authors.html')
    elif request.method == "POST" and :
        author_to_add['first_name'] = request.form['author_first']
        author_to_add['last_name'] = request.form['author_last']
        birth_year = request.form['birth_year']
        birth_month = request.form['birth_month']
        birth_day = request.form['birth_day']
        author_to_add['date_of_birth'] = birth_year+'-'+birth_month+'-'+birth_day
        author_to_add['origin'] = request.form['origin']
        author_id = queries.post_author(author_to_add)[0]
        print('author_id: ' + str(author_id))
        book_to_add = {}
        book_to_add['author_id'] = author_id
        book_to_add['title'] = request.form['title']
        book_to_add['user_id'] = request.form['user_id']
        book_to_add['genre_id'] = request.form['genre_id']
        book_to_add['position'] = request.form['position']
        book_to_add['release_year'] = request.form['release_year']
        queries.post_book(book_to_add)
        return redirect('/books')


if __name__ == "__main__":
    app.run(debug=True)