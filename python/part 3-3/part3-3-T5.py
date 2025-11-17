num = int(input("Please type in a number:"))
num1 = 1
num2 = num
while num1 <= num2:
    if num1 != num2:
        print(num1)
        print(num2)
        num1 += 1
        num2 -= 1
    else:
        print(num1)
        break