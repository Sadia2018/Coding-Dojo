from app.config.mysqlconnection import connectToMySQL
from flask import flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
from app.models import user

# class modelled after the database table.
class Sighting:
    db_name = 'sasquatch_websighting'
    def __init__(self, data):
        self.id = data['id']
        self.location = data['location']
        self.date_of_sighting = data['date_of_sighting']
        self.what_happened = data['what_happened']
        self.number_of_sasquatches = data['number_of_sasquatches']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

# static mehtod to validate the sightings. 
    @staticmethod
    def validate(sight):
        is_valid = True
        if sight['location'] == '':
            is_valid = False
            flash('Please enter a location')
        if sight['what_happened'] == '':
            is_valid = False
            flash('Please enter what happened')
        if sight['date_of_sighting'] == '':
            is_valid = False
            flash('Please enter the sight date')
        if sight['number_of_sasquatches'] == '0':
            is_valid = False
            flash('Please enter at least 1 sasquatch')
        return is_valid

# class method to save a sighting. 
    @classmethod
    def save(cls, data):
        query = 'INSERT INTO sightings (location, date_of_sighting, what_happened, number_of_sasquatches, users_id) VALUES ( %(location)s, %(date_of_sighting)s, %(what_happened)s, %(number_of_sasquatches)s, %(users_id)s );'
        return connectToMySQL(cls.db_name).query_db(query, data)

# class method to delete a sight.
    @classmethod
    def delete(cls, data):
        query = "DELETE FROM sightings WHERE id = %(id)s;"
        return connectToMySQL(cls.db_name).query_db(query, data)

# class method to retrive one sighting.
    @classmethod
    def get_one(cls,data):
        query = "SELECT * FROM sightings WHERE id = %(id)s;"
        results = connectToMySQL(cls.db_name).query_db(query, data)
        if len(results) < 1:
            return False
        return cls(results[0])
# class method to update a user. 
    @classmethod
    def update(cls, data):
        q = "UPDATE sightings SET location=%(location)s, date_of_sighting=%(date_of_sighting)s, what_happened=%(what_happened)s, number_of_sasquatches=%(number_of_sasquatches)s WHERE id = %(id)s;"
        return connectToMySQL(cls.db_name).query_db(q, data)
