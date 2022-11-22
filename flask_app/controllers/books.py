from flask_app import app
from flask_app.models import author
from flask_app.models import book
from flask_app.models import favorite
from flask import render_template, redirect, request

@app.route('/books')
def all_books():
    books = book.Book.get_all_books()
    return render_template('books.html', books = books)

@app.route('/create_book', methods = ['POST'])
def create_book():
    data = {
        'title': request.form['title'],
        'num_of_pages': request.form['num_of_pages']
    }
    book.Book.create_book(data)
    return redirect(request.referrer)

@app.route('/show_book/<int:id>')
def show_book(id):
    authors = author.Author.get_all_authors()
    books = book.Book.get_all_books()
    data = {
        'book_id': id
    }
    for x in books:
        if x.id == id:
            the_book = x
    fav_authors = favorite.Favorite.get_all_fav_authors(data)
    return render_template('book_show.html', book = the_book, fav_authors = fav_authors, authors = authors)

@app.route('/fav_authors/<int:id>', methods = ['POST'])
def fav_authors(id):
    data = {
        'author_id': request.form['fav_author'],
        'book_id': id
    }
    favorite.Favorite.add_fav(data)
    return redirect(f"/show_book/{data['book_id']}")