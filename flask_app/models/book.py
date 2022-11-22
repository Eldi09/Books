from flask_app.config.mysqlconnection import connectToMySQL

class Book:
    db_name = "books_schema"
    def __init__(self, data):
        self.id = data['id']
        self.title = data['title']
        self.num_of_pages = data['num_of_pages']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    @classmethod
    def create_book(cls, data):
        query = "INSERT INTO books (title, num_of_pages) VALUES(%(title)s, %(num_of_pages)s)"
        return connectToMySQL(cls.db_name).query_db(query, data)

    @classmethod
    def get_all_books(cls):
        query = "SELECT * FROM books;"
        results = connectToMySQL(cls.db_name).query_db(query)
        books = []
        for the_book in results:
            books.append(cls(the_book))
        return books