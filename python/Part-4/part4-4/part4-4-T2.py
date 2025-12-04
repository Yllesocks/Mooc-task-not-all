num = int(input("Please type in a positive integer:"))

index = num - num * 2
for i in range(num * 2 + 1):
    if index == 0:
        index += 1
        continue
    else:
        print(index)
        index += 1