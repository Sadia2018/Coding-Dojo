for x in range(0,150):
    print(x)

# # multiples of 5 from 5 - 1000

for i in range(5,1000,5):
    print(i)

# # integers 1 - 100. Print "coding" if /5. Print "coding dojo" if /10

for y in range(1,100):
    if y % 5 == 0:
        print(y,"coding")
    elif y % 10 == 0:
        print(y,"dojo")

# add odd integers. print final sum

for i in range(0,500000):
    if i % 2 != 0:
        x = i 
        sum(x)

# positive numbers. countdown from 2018 by 4. 

for i in range(2018,0,-4):
    print(i)

#lowNum. highNum. Mult
lowNum = 2
highNum = 10
mult = 2

for i in range(lowNum, highNum, mult):
    print(i)