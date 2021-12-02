from app.config.mysqlconnection import connectToMySQL
from flask import flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
from app.models import user

# class modelled after the database table.
class Car:
    db_name = 'belt_exam'
    def __init__(self, data):
        self.id = data['id']
        self.make = data['make']
        self.model = data['model']
        self.year = data['year']
        self.price = data['price']
        self.description = data['description']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

# static mehtod to validate the Cars. 
    @staticmethod
    def validate(car):
        is_valid = True
        if car['make'] == '':
            is_valid = False
            flash('Please enter a make')
        if car['model'] == '':
            is_valid = False
            flash('Please enter model')
        if car['year'] == '':
            is_valid = False
            flash('Please enter an year')
        if car['price'] == '0':
            is_valid = False
            flash('Please enter a price')
        if car['description'] == '':
            is_valid = False
            flash('Please enter a description')
        return is_valid

# class method to save a Car. 
    @classmethod
    def save(cls, data):
        query = 'INSERT INTO cars (make, model, year, price, description, users_id) VALUES ( %(make)s, %(model)s, %(year)s, %(price)s, %(description)s, %(users_id)s );'
        return connectToMySQL(cls.db_name).query_db(query, data)

# class method to delete a sight.
    @classmethod
    def delete(cls, data):
        query = "DELETE FROM cars WHERE id = %(id)s;"
        return connectToMySQL(cls.db_name).query_db(query, data)

# class method to retrive one Car.
    @classmethod
    def get_one(cls,data):
        query = "SELECT * FROM cars WHERE id = %(id)s;"
        results = connectToMySQL(cls.db_name).query_db(query, data)
        if len(results) < 1:
            return False
        return cls(results[0])

# class method to update a user. 
    @classmethod
    def update(cls, data):
        q = "UPDATE cars SET make=%(make)s, model=%(model)s, year=%(year)s, price=%(price)s, description=%(description)s WHERE id = %(id)s;"
        return connectToMySQL(cls.db_name).query_db(q, data)