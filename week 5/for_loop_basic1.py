for x in range(0,150):
    print(x)

# # multiples of 5 from 5 - 1000

for i in range(5,1000,5):
    print(i)

# # integers 1 - 100. Print "coding" if /5. Print "coding dojo" if /10

for i in range(1,100):
    if i % 10 == 0:
        print("coding")
    elif i % 5 == 0:
        print("dojo")
    else:
        print(i)

# add odd integers. print final sum
def addOdd():
    sum = 0
    for i in range(0,500000):
        if i % 2 != 0:
            sum += i
    return sum
print(addOdd())


# positive numbers. countdown from 2018 by 4. 

for i in range(2018,0,-4):
    print(i)

#lowNum. highNum. Mult
lowNum = 2
highNum = 10
mult = 2

for i in range(lowNum, highNum, mult):
    print(i)