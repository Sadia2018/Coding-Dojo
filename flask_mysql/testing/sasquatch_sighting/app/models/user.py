from app.config.mysqlconnection import connectToMySQL
from flask import flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
from app.models import sighting
from app.models.sighting import Sighting


# class modelled after the database table. 
class User:
    db_name = 'sasquatch_websighting'
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.sightings = []

# static methdod to validate form data
    @staticmethod
    def validate(user):
        is_valid = True
        query = 'SELECT * FROM users WHERE email = %(email)s;'
        results = connectToMySQL('sasquatch_websighting').query_db(query, user)
        if len(results) >= 1:
            is_valid = False
            flash('Email address already exits. Please use another email')
        if len(user['first_name']) < 2:
            is_valid = False
            flash('First Name must be 2 characters long')
        if len(user['last_name']) < 2:
            is_valid = False
            flash('Last Name must 2 characters long')
        if not EMAIL_REGEX.match(user['email']):
            is_valid = False
            flash("Please enter a valid email address")
        if len(user['password']) < 8:
            is_valid = False
            flash('Password must be at least 8 characters long')
        if user['password'] != user['confirm']:
            is_valid = False
            flash("Passwords must match.")
        return is_valid

# class method to save data into the database. 
    @classmethod
    def save(cls, data):
        query = 'INSERT INTO users (first_name, last_name, email, password) VALUES ( %(first_name)s, %(last_name)s, %(email)s, %(password)s );'
        return connectToMySQL(cls.db_name).query_db(query, data)

# class method to retrive all users.
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL(cls.db_name).query_db(query)
        users = []
        for user in results:
            users.append(cls(user))
        return users

# class method to retrive one user.
    @classmethod
    def get_one(cls,data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        results = connectToMySQL(cls.db_name).query_db(query, data)
        if len(results) < 1:
            return False
        return cls(results[0])

# class method to get a user by email. --- can be updated for username.
    @classmethod
    def get_email(cls, data):
        query = "SELECT * FROM users WHERE email = %(email)s"
        results = connectToMySQL(cls.db_name).query_db(query, data)
        if len(results) < 1:
            return False
        return cls(results[0])

# class method to update a user. 
    @classmethod
    def update(cls, data):
        q = "UPDATE users SET first_name=%(first_name)s, last_name=%(last_name)s WHERE id = %(id)s;"
        return connectToMySQL(cls.db_name).query_db(q, data)

# class method to delete a user.
    @classmethod
    def delete(cls, data):
        query = "DELETE FROM users WHERE id = %(id)s;"
        return connectToMySQL(cls.db_name).query_db(query, data)

# instance method to get a users full name 
    def full_name(self):
        return f"{self.first_name} {self.last_name}"


# class method to get all sightings that belong to a user. 
    # @classmethod
    # def get_sightings_with_user(cls, data):
    #     query = "SELECT * FROM users LEFT JOIN sightings ON users.id = sightings.users_id WHERE users.id = %(id)s;"
    #     results = connectToMySQL(cls.db_name).query_db(query,data)
    #     print(results)
    #     sightings = []
    #     for row_from_db in results:
    #         sight_data = {
    #             'id': row_from_db['sightings.id'],
    #             'location' : row_from_db['location'],
    #             'date_of_sighting' : row_from_db['date_of_sighting'],
    #             'first_name': row_from_db['first_name'],
    #             'last_name': row_from_db['last_name']
    #         }
    #         sightings.append(sight_data)

# class method. 
    @classmethod
    def get_all_users_sighting(cls):
        query = "SELECT * FROM users JOIN sightings ON users.id = sightings.users_id;"
        results = connectToMySQL(cls.db_name).query_db(query)
        print(results)
        all_sightings = []
        for row in results:
            user_instance = User(row)
            data = {
                'id': row['sightings.id'],
                'location' : row['location'],
                'date_of_sighting' :row['date_of_sighting'],
                'what_happened': row['what_happened'],
                'number_of_sasquatches':row['number_of_sasquatches'],
                'created_at':row['sightings.created_at'],
                'updated_at': row['sightings.updated_at']
            }
            user_instance.sighting = Sighting(data)
            all_sightings.append(user_instance)
        return all_sightings
