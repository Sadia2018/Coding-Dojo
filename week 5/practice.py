x = [5,34,10,1,6]
x += [2]
print(x)

x = [4,5,6]

if not x:
    print('it does not contain')

weekend = {"Sun": "Sunday", "Sat": "Saturday"} #literal notation
capitals = {} #create an empty dictionary then add values
capitals["svk"] = "Bratislava"
capitals["deu"] = "Berlin"
capitals["dnk"] = "Copenhagen"

print(weekend.items())

weekend_2 = weekend.copy()
print(weekend_2)

print(weekend["Sun"])

value_removed = weekend.pop("Sun")
print(weekend)
print(value_removed)

del weekend["Sat"]
print(weekend)

def add(a,b):	# function name: 'add', parameters: a and b
    x = a + b	# process
    return x	# return value: x

sum = add(10,22)
print(sum)

set defaults when declaring the parameters
def be_cheerful(name='a$$hole', repeat=2):
	print(f"good morning {name}\n" * repeat)
# be_cheerful()    # output: good morning (repeated on 2 lines)
# be_cheerful("tim")    # output: good morning tim (repeated on 2 lines)
# be_cheerful(name="john")    # output: good morning john (repeated on 2 lines)
# be_cheerful(repeat=6)    # output: good morning (repeated on 6 lines)
# be_cheerful(name="michael", repeat=5)    # output: good morning michael (repeated on 5 lines)
# # NOTE: argument order doesn't matter if we are explicit when sending in our arguments!
# be_cheerful(repeat=3, name="kb")    # output: good morning kb (repeated on 3 lines)

be_cheerful(repeat = 4, name = "raphael")

def multiply(num_list, num):
    for x in num_list:
        x *= num 
    return num_list
num_list = [2,4,10,16]
num = 5
print(multiply(num_list, num))
