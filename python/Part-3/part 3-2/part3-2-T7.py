while True:
    string = input("Please type in a string:")
    dash_len = len(string)
    print(string)
    print("-" * dash_len)
    if string == "":
        break