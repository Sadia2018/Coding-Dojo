#import the function from mysqlconnection that will return an instance of a connection. 
from app.config.mysqlconnection import connectToMySQL


# ninja class modelled after our dojo table in the database.
class Ninja:
    def __init__(self, data):
        self.id - data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.dojos_id = data['dojos_id']

# class method to insert a new ninja
    @classmethod
    def new_ninja(cls, data):
        query = "INSERT INTO ninjas ( first_name, last_name, age, created_by, updated_by, dojos_id) VALUES ( %(fname)s, %(lname)s, %(age)s, NOW(), NOW(), %(dojos_id));"
        return connectToMySQL('dojos_and_ninja_schema').query_db(query, data)