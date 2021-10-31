#import the function from mysqlconnection that will return an instance of a connection. 
from app.config.mysqlconnection import connectToMySQL
from app.models import ninja


# dojo class modelled after our dojo table in the database. 
class Dojo:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

# class method to retrive all dojos. 
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL('dojos_and_ninja_schema').query_db(query)
        dojos = []
        for dojo in results:
            dojos.append(cls(dojo))
        return dojos

#class method to add a new dojo to database
    @classmethod
    def new_dojo(cls, data):
        query = "INSERT INTO dojos (name, created_at, updated_at) VALUES (%(dname)s, NOW(), NOW() );"
        return connectToMySQL('dojos_and_ninja_schema').query_db(query, data)

# class method to get one dojo 
    @classmethod
    def one_dojo(cls,data):
        query = "SELECT * FROM dojos LEFT JOIN ninjas ON ninjas.dojos_id = dojos.id WHERE dojos.id = %(id)s; "
        results = connectToMySQL('dojos_and_ninja_schema').query_db(query, data)
        ninjas =[]
        for row_from_db in results:
            ninjas.append(cls(row_from_db))
        return ninjas