from flask_app import app
from flask_app.models import author
from flask_app.models import book
from flask_app.models import favorite
from flask import render_template, redirect, request

@app.route('/')
def index():
    authors = author.Author.get_all_authors()
    return render_template("authors.html", authors = authors)

@app.route('/create_author', methods = ['POST'])
def create_author():
    data = {
        'name': request.form['name']
    }
    author.Author.create_author(data)
    return redirect('/')

@app.route('/show_author/<int:id>')
def show_author(id):
    authors = author.Author.get_all_authors()
    books = book.Book.get_all_books()
    data = {
        'author_id': id
    }
    for x in authors:
        if x.id == id:
            the_author = x
    fav_books = favorite.Favorite.get_all_fav_books(data)
    return render_template('author_show.html', author = the_author, books = books, fav_books = fav_books)

@app.route('/fav_book/<int:id>', methods = ['POST'])
def fav_book(id):
    data = {
        'author_id': id,
        'book_id': request.form['fav_book']
    }
    favorite.Favorite.add_fav(data)
    return redirect(f"/show_author/{data['author_id']}")
