from flask import flash
from app.config.mysqlconnection import connectToMySQL

class Dojo:
    db_name = 'dojo_survey_schema'
    result = connectToMySQL('dojo_survey_schema')
    def __init__(self , data):
        self.id = data['id']
        self.name = data['name']
        self.location = data['location']
        self.language = data['language']
        self.comment = data['comment']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

#---- class method to retrive all dojos from database
    @classmethod
    def get_all(cls):
        query = 'SELECT * FROM dojos;'
        results_from_db = connectToMySQL(cls.db_name).query_db(query)

        all_dojos = []
        for row in results_from_db:
            all_dojos.append(cls(row))
        print(all_dojos)
        return all_dojos

#---- static method to validate form data 
    @staticmethod
    def validate_dojo(dojo):
        is_valid = True
        if len(dojo['name']) < 3:
            flash('Name must be at least 3 characters long')
            is_valid = False
        if dojo['location'] == "":
            flash('Must select a location')
            is_valid = False
        if dojo['language'] == "":
            flash('Must pick a programming langauge to learn')
            is_valid = False
        return is_valid
