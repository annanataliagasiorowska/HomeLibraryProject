from flask import Flask, render_template, request, redirect

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
        return render_template('new_books.html')
    else:
        book_to_add['title'] = request.form['title']
        author_first_name = request.form['author_first']
        author_last_name = request.form['author_last']
        author_id = queries.find_author_id(author_first_name, author_last_name)
        book_to_add['release_year'] = request.form['release_year']
        book_to_add['author_id'] = author_id
        owner = request.form['owner_name']
        print(owner)
        user_id = queries.find_user_id(owner)
        book_to_add['user_id'] = user_id
        queries.post_book(book_to_add)
        return redirect('/books.html')


if __name__ == "__main__":
    app.run(debug=True)