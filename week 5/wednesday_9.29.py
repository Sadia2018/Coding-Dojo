# pass. when we need function but dont know exactly what it will take. place holder. 

def nextFunction():
    pass

"""
Parks Business
"""
def print_parks(a):
    for p in a:
        print("The Parks: ", p)
# gives us the whole park data set. 

#loops through the entire data set and pulls zooName
def print_parkNames(a):
    for p in a:
        print(p["zooName"])

printParkNames(parks)