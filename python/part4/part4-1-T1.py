while True:
    name = input("Editor:")
    if name.lower() == "visual studio code":
        print("an excellent choice!")
        break
    elif name.lower() == "notepad" or name.lower() == "word":
        print("awful")
    else:
        print("not good")