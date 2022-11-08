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
    pages_all, offset = count_offset(page)
    return jsonify(queries.get_books_all(offset, LIMIT))


def count_offset(page):
    number_of_books = queries.count_books()[0]['count']
    pages_all = number_of_books // LIMIT + 1
    offset = (page - 1) * LIMIT
    return pages_all, offset


@app.route("/books")
def books():
    page = int(request.args.get('page', 1))
    pages_all, offset = count_offset(page)
    return render_template('books.html', page=page, pages_all=pages_all)


@app.route("/authors")
def authors():
    return render_template('authors.html')


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
        genre_id = queries.find_genre_id(genre)
        book_to_add['genre_id'] = genre_id
        book_to_add['position'] = request.form['position_name']
        author_first_name = request.form['author_first']
        author_last_name = request.form['author_last']
        author_id = queries.find_author_id(author_first_name, author_last_name)
        if author_id:
            book_to_add['author_id'] = author_id['id']
        else:
            return render_template('new_authors.html')
        book_to_add['release_year'] = request.form['release_year']
        queries.post_book(book_to_add)
        return redirect('/books')


@app.route("/new_authors", methods=["GET", "POST"])
# @login_required
def add_author():
    author_to_add = {}
    if request.method == "GET":
        pass
        # TODO page authors, query
        # authors = queries.get_authors_all()
        # return render_template('authors.html', authors=authors)
    else:
        author_to_add['first_name'] = request.form['author_first']
        author_to_add['last_name'] = request.form['author_last']
        birth_year = request.form['birth_year']
        birth_month = request.form['birth_month']
        birth_day = request.form['birth_day']
        author_to_add['date_of_birth'] = birth_year+'-'+birth_month+'-'+birth_day
        author_to_add['origin'] = request.form['origin']
        print('dane autora:' + str(author_to_add))
        queries.post_author(author_to_add)
        return redirect('/books')


if __name__ == "__main__":
    app.run(debug=True)