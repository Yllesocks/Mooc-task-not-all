import math
while True:
    n = int(input("Please type in a number:"))
    if n < 0:
        print("Thanks and bye!")
        break
    else:
        print(math.factorial(n))