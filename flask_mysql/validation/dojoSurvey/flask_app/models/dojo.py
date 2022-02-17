from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import app, flash

class Dojo:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.location = data['location']
        self.language = data['language']
        self.comment = data['comment']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL('survey').query_db(query)
        surveys = []
        for a in results:
            surveys.append(cls(a))

        return surveys

    @classmethod
    def save(cls, data):
        query = "INSERT INTO dojos(name,location,language,comment) VALUES (%(name)s,%(location)s, %(language)s, %(comment)s);"
        result = connectToMySQL('survey').query_db(query, data)
        return result

    @staticmethod
    def validate_survey(survey):
        is_valid = True # we assume this is true
        if len(survey['name']) < 3:
            flash("Name must be at least 3 characters.")
            is_valid = False
        if survey['location'] == "None":
            flash("Must choose a location")
            is_valid = False
        if survey['language'] == "None":
            flash("Must choose a location")
            is_valid = False
        if len(survey['comment']) < 1:
            flash("Enter a valid comment.")
            is_valid = False
        return is_valid