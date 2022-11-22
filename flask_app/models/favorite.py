from flask_app.config.mysqlconnection import connectToMySQL

class Favorite:
    db_name = "books_schema"
    def __init__(self, data):
        self.author_id = data['author_id']
        self.book_id = data['book_id']

    @classmethod
    def add_fav(cls, data):
        query = "INSERT INTO favorites (author_id, book_id) VALUES (%(author_id)s, %(book_id)s);"
        return connectToMySQL(cls.db_name).query_db(query, data)

    @classmethod
    def get_all_fav_books(cls, data):
        query = "SELECT books.id, books.title, books.num_of_pages FROM books LEFT JOIN favorites ON favorites.book_id = books.id LEFT JOIN authors ON favorites.author_id = authors.id WHERE authors.id = %(author_id)s;"
        results = connectToMySQL(cls.db_name).query_db(query, data)
        return results
    
    @classmethod
    def get_all_fav_authors(cls, data):
        query = "SELECT authors.id, authors.name FROM authors LEFT JOIN favorites ON favorites.author_id = authors.id LEFT JOIN books ON favorites.book_id = books.id WHERE books.id = %(book_id)s;"
        results = connectToMySQL(cls.db_name).query_db(query, data)
        return results