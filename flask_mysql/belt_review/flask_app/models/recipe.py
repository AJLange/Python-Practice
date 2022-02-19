from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import app
from flask import flash
from datetime import datetime


class Recipe:
    db = ("cookbook")
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.time_over= data['time_over']
        self.date_made = data['date_made']
        self.instructions= data['instructions']
        self.description = data['description']
        self.created_on = data['created_on']
        self.updated_on = data['updated_on']
        self.user_id = data['user_id']
        
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM recipes;"
        results = connectToMySQL(cls.db).query_db(query)
        recipes = []
        for r in results:
            recipes.append( cls(r) )
        return recipes
    
    @classmethod
    def get_by_id(cls,data):
        query = "SELECT * FROM recipes WHERE id = %(id)s;"
        results = connectToMySQL(cls.db).query_db(query,data)
        return cls(results[0])

    @classmethod
    def save(cls,data):
        query = "INSERT INTO recipes (name,instructions,description,time_over,date_made,user_id) VALUES (%(name)s,%(instructions)s,%(description)s,%(time_over)s,%(date_made)s,%(user_id)s);"
        return connectToMySQL(cls.db).query_db(query,data)

    @classmethod
    def destroy(cls,data):
        query = "DELETE FROM recipes WHERE recipes.id = %(id)s;"
        return connectToMySQL(cls.db).query_db(query,data)

    @classmethod
    def update(cls,data):
        query = "UPDATE recipes SET name =%(name)s, description= %(description)s, instructions= %(instructions)s, time_over = %(time_over)s, date_made = %(date_made)s, updated_on = NOW(), WHERE id = %(id)s;"
        return connectToMySQL(cls.db).query_db(query,data)