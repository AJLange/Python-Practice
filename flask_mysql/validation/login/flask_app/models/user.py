from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import app
from flask import flash

import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
PSW_REGEX = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$')

class User:
    db = ("registration")
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL('registration').query_db(query)
        users = []
        for a in results:
            users.append(cls(a))

        return users

    @classmethod
    def save(cls, data):
        query = "INSERT INTO users(first_name,last_name,email,password) VALUES (%(first_name)s,%(last_name)s, %(email)s, %(password)s);"
        result = connectToMySQL('registration').query_db(query, data)
        return result

    @classmethod
    def get_by_email(cls, data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        result = connectToMySQL('registration').query_db(query, data)
        # no matching user
        if len(result) <1:
            flash("No matching user in DB", "login")
            return False
        return cls(result[0])

    @classmethod
    def get_by_id(cls, data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        result = connectToMySQL('registration').query_db(query, data)
        # no matching user
        if len(result) <1:
            flash("No matching user in DB", "login")
            return False
        return cls(result[0])

    @staticmethod
    def validate_reg(survey):
        is_valid = True # we assume this is true
        results = connectToMySQL(User.db).query_db("SELECT * FROM users WHERE email = %(email)s;", survey)
        if len(results) >=1:
            flash("Email already registered", "register")
            is_valid = False
        if len(survey['first_name']) < 3:
            flash("First name must be at least 3 characters.", "register")
            is_valid = False
        if len(survey['last_name']) < 3:
            flash("Last name must be at least 3 characters.", "register")
            is_valid = False
        if len(survey['password']) < 8:
            flash("Password should be at least 8 chars", "register")
            is_valid = False
        if survey['password_c'] != survey['password']:
            flash("Passwords do not match!", "register")
            is_valid = False
        if not EMAIL_REGEX.match(survey['email']):
            flash("Invalid Email address!", "register")
            is_valid = False
        if not PSW_REGEX.match(survey['password']):
            flash("Passwords must contain lowercase letter, one uppercase, and one number", "register")
            is_valid = False
        return is_valid

    @staticmethod
    def validate_login(survey):
        is_valid = True # we assume this is true

        if len(survey['password']) < 3:
            flash("Wrong Password!", "login")
            is_valid = False

        return is_valid