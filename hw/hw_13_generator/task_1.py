def fibonacci_generator(x):
    dig1, dig2 = 0, 1
    for i in range(x):
        dig1, dig2 = dig2, dig1 + dig2
        yield dig1

x = int(input("Enter digital: "))
print(list(fibonacci_generator(x)))
