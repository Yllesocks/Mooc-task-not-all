list = []
HMI = int(input("How many items:"))
index = 1
while HMI >= index:
    num = int(input(f"Item {index}:"))
    list.append(num)
    index += 1
print(list)