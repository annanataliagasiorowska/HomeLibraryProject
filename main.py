from flask import Flask, jsonify, render_template, request, redirect

import queries

app = Flask(__name__)
app.secret_key = 'ghbdtn93vbh65bdctv407yfv'


@app.route("/")
@app.route("/index")
def index():
    return render_template('index.html')


@app.route("/books")
def books():
    books = queries.get_books_all()
    return render_template('books.html', books=books)


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
        print(owner)
        user_id = queries.find_user_id(owner)
        book_to_add['user_id'] = user_id
        genre = request.form['genre']
        genre_id = queries.find_genre_id(genre)
        book_to_add['genre_id'] = genre_id
        book_to_add['position'] = request.form['position']
        author_first_name = request.form['author_first']
        author_last_name = request.form['author_last']
        author_id = queries.find_author_id(author_first_name, author_last_name)
        if author_id:
            book_to_add['author_id'] = author_id
        else:
            render_template('new_authors.html')
        book_to_add['release_year'] = request.form['release_year']
        queries.post_book(book_to_add)
        return redirect('/books.html')


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
        author_to_add['first_name'] = request.form['first_name']
        author_to_add['last_name'] = request.form['last_name']
        author_to_add['birth_year'] = request.form['birth_year']
        author_to_add['origin'] = request.form['origin']
        queries.post_author(author_to_add)
        return redirect('/books.html')


@app.route('/api/books')
def display_books():
    return jsonify(queries.get_books_all())


if __name__ == "__main__":
    app.run(debug=True)