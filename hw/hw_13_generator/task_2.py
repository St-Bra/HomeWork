def infin(x):
    while True:
        for digit in range(1,x+1):
            yield digit



x = int(input("Enter digital: "))
a = infin(x)

for i in a:
    print(i, end='-')