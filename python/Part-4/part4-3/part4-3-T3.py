list = []
index = 1
while True:
    print(list)
    task = input("a(d)d, (r)emove or e(x)it:")
    if task == "d":
        list.append(index)
        index += 1
    elif task == "r":
        list.remove(index - 1)
        index -= 1
    else:
        print("Bye!")
        break