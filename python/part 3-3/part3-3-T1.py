num = int(input("Please type in a number:"))

num_1 = 1
while num_1 <= num:
    num_2 = 1
    while num_2 <= num:
        print(f"{num_1} x {num_2} = {num_1 * num_2}")
        num_2 += 1
    num_1 += 1