from app.config.mysqlconnection import connectToMySQL
from flask import flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 
# import second class.

# class modelled after the database table. 
class User:
    db_name = 'user_login_registration'
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

# static methdod to validate form data
    @staticmethod
    def validate(user):
        is_valid = True
        query = 'SELECT * FROM users WHERE email = %(email)s;'
        results = connectToMySQL('user_login_registration').query_db(query, user)
        if len(results) >= 1:
            is_valid = False
            flash('Email address already exits. Please use another email')
        if len(user['first_name']) < 2:
            is_valid = False
            flash('First Name must be 2 characters long')
        if len(user['last_name']) < 2:
            is_valid = False
            flash('Last Name must 2 characters long')
        if not Email_REGEX.match(user['email']):
            is_valid = False
            flash('Invalid email address')
        if len(user['password']) < 8:
            is_valid = False
            flash('Password must be at least 8 characters long')
        if user['password'] != user['confirm']:
            is_valid = False
            flash("Your passwords don't match")
        return is_valid
