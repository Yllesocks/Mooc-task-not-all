num = int(input("Please type in a number:"))

num_1 = 1
num_2 = 1

while True:

    if num_1 * num < num * num:
        break
    elif num_1 == num:
        num_1 =1
        num_2 += 1
        print(f"{num_1}X{num_2}={num_1 * num_2}")
    else:
        print(f"{num_1}X{num_2}={num_1 * num_2}")
    num_1 += 1
