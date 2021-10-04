x = [ [5,2,3], [10,8,9] ] 
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

# # Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] 
x[1][0] = 15
print(x)
# # Change the last_name of the first student from 'Jordan' to 'Bryant
students[0]['last_name'] = 'Bryant'
print(students)
# # In the sports_directory, change 'Messi' to 'Andres'
sports_directory['soccer'][0] = 'Andres'
print(sports_directory)
# # Change the value 20 in z to 30
z[0]['y'] = 30
print(z)

#function iterateDictionary()

students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

def interateDictionary(list):
    for i in range(len(list)):
        print(list[i])
print(interateDictionary(students))

# function interateDictionary 2 - key

def interateDictionary_key(name,list):
    for i in range(len(list)):
        for key, value in list[i].items():
            if key == name:
                print(value)

interateDictionary_key('first_name', students)

dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
def print_info(dictionary):
    for k in dictionary:
        print(k)
        print(len(dictionary[k]))
        print(dictionary[k])
print_info(dojo)


