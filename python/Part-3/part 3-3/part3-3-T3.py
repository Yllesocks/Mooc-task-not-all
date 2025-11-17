while True:
    num1 = int(input("Please type in a number:"))
    num = num1
    out_num = 1
    while num > 0:
        out_num = num * out_num
        num -= 1
    if out_num > 0 and num1 > 0:
        print(f"The factorial of the number {num1} is {out_num}")
    else:
        print("Thanks and bye!")
        break