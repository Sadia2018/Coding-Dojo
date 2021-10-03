new_list = []
def countdown(num):
    for i in range(num,-1,-1):
        print(i)
        new_list.append(i)
    print(new_list)
countdown(5)

list = [1,2]
def print_and_return(list):
    print(list[0])
    x = list[1]
    return x
print_and_return(list)

list = [3,5,6]
def first_plus_length(list):
    x = len(list)
    return list[0] + x
print(first_plus_length(list))

list = [5,2,3,2,1,4]
new_list = []
def values_greater_than_second(list):
    for i in list:
        if i > 2:
            new_list.append(i)
    print(len(new_list))
    return new_list
print(values_greater_than_second(list))


def this_length_that_value(length,value):
    new_list = []
    for i in range(0,length):
        new_list.append(value)
    return new_list
print(this_length_that_value(5,7))