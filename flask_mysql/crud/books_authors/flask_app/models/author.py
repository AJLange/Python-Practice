from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import app

class Author:
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    @classmethod
    def get_all(cls):
        query="SELECT * FROM authors;"
        results = connectToMySQL('books_schema').query_db(query)
        authors = []
        for a in authors:
            authors.append(cls(a))
        return results

    @classmethod
    def save(cls, data):
        query = "INSERT INTO authors (name) VALUES (%(name)s);"

        result = connectToMySQL('books_schema').query_db(query,data)
        return result

    @classmethod
    def get_one_with_books(cls, data):
        query = "SELECT * FROM authors LEFT JOIN books WHERE id=data;"
        result =  connectToMySQL('books_schema').query_db(query,data)
        return result