for x in range(0,150):
    print(x)

# multiples of 5 from 5 - 1000

for i in range(5,1000,5):
    print(i)

# integers 1 - 100. Print "coding" if /5. Print "coding dojo" if /10

for y in range(1,100):
    if (y % 5 == 0):
        print(y,"coding")
    elif (y % 10 == 0):
        print(y,"dojo")
