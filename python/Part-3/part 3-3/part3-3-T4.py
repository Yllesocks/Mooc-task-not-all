num = int(input("Please type in a number:"))
num1 = 2
num2 = 1
while num % 2 == 0 and num1 <= num:
    print(num1)
    print(num2)
    num1 += 2
    num2 += 2
while num % 2 != 0:
    if num1 > num:
        print(num)
        break
    print(num1)
    print(num2)
    num1 += 2
    num2 += 2