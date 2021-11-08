from app.config.mysqlconnection import connectToMySQL
from flask import flash

# class modelled after the database table. 
class Recipe:
    db_name ='receipes'
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.under_30_minutes = data['under_30_minutes']
        self.instructions = data['instructions']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.users_id = data['users_id']

#static method to validate recipe form data. 
    @staticmethod
    def validate(recipe):
        is_valid = True
        if len(recipe['name']) < 2:
            is_valid = False
            flash('Recipe name must be at least 2 characters long')
        if len(recipe['description']) < 2:
            is_valid = False
            flash('Please enter a full description of the recipe')
        if len(recipe['instructions']) < 2:
            is_valid = False
            flash('Please enter all the instructions for the recipe')
        if 'under_30_minutes' not in recipe:
            is_valid = False
            flash('Please select if the recipe is under 30 minutes or not')
        if recipe['created_at'] == '':
            is_valid = False
            flash('Please select a date')
        return is_valid

#class method to save a recipe into the database
    @classmethod
    def save(cls, data):
        query = "INSERT INTO receipes (name, description, instructions, under_30_minutes, created_at, users_id ) VALUES ( %(name)s, %(description)s, %(instructions)s, %(under_30_minutes)s, %(created_at)s, %(users_id)s );"
        return connectToMySQL(cls.db_name).query_db(query, data)
    
    @classmethod
    def get_user(cls):
        query = "SELECT * FROM receipes LEFT JOIN users ON receipes.users_id = users.id;"
        results = connectToMySQL(cls.db_name).query_db(query)
        recipes = []
        for recipe in results:
            data = {
                'name':recipe['name'],
                'under_30_minutes':recipe['under_30_minutes']
            }
            recipes.append(data)
        return recipes