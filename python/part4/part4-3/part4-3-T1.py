list = [1, 2, 3, 4, 5]
while True:
    index = int(input("Index:"))
    if index < 0:
        break
    else:
        new_value = int(input("New value:"))
        list[index] = new_value
        print(list)