num1 = 42  #variable declaration
num2 = 2.3 # variable declaration
boolean = True 
string = 'Hello World' # data type, primitive
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] # list, intialize value
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} #dictionary, intialize value
fruit = ('blueberry', 'strawberry', 'banana') #tuple, intialize value
print(type(fruit)) #log statement
print(pizza_toppings[1]) #log statement
pizza_toppings.append('Mushrooms') #list,add value
print(person['name']) #log statement        
person['name'] = 'George' #dictionary, change value
person['eye_color'] = 'blue' #dictionary, add value
print(fruit[2]) #log statement

if num1 > 45:                   #conditional if else statement
    print("It's greater")
else:
    print("It's lower")

if len(string) < 5:                  #conditional statement, length check
    print("It's a short word!")
elif len(string) > 15:
    print("It's a long word!")
else:
    print("Just right!")

for x in range(5):    # log statement
    print(x)
for x in range(2,5):
    print(x)
for x in range(2,10,3):
    print(x)
x = 0
while(x < 5):  # while loop 
    print(x)
    x += 1

pizza_toppings.pop()    # function  
pizza_toppings.pop(1)   # function 

print(person)                    #log statement 
person.pop('eye_color')          # function, parameter 
print(person)

for topping in pizza_toppings:    # conditional statement 
    if topping == 'Pepperoni':
        continue
    print('After 1st if statement')
    if topping == 'Olives':
        break

def print_hello_ten_times():    
    for num in range(10):   # for loop      
        print('Hello')

print_hello_ten_times()  # function 

def print_hello_x_times(x):   # function 
    for num in range(x):   # for loop
        print('Hello')

print_hello_x_times(4) #log statement 

def print_hello_x_or_ten_times(x = 10): 
    for num in range(x): 
        print('Hello')

print_hello_x_or_ten_times()   
print_hello_x_or_ten_times(4)



"""
Bonus section
"""

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)