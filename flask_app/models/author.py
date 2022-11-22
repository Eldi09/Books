from flask_app.config.mysqlconnection import connectToMySQL

class Author:
    db_name = "books_schema"
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    @classmethod
    def create_author(cls, data):
        query = "INSERT INTO authors (name) VALUES (%(name)s)"
        return connectToMySQL(cls.db_name).query_db(query, data)

    @classmethod
    def get_all_authors(cls):
        query = "SELECT * FROM authors;"
        results = connectToMySQL(cls.db_name).query_db(query)
        authors = []
        for author in results:
            authors.append(cls(author))
        return authors

    @classmethod
    def get_fav_books(cls, data):
        return 