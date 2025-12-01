index = 1
list = []
while True:
    word = input("Word:")
    if word in list:
        print(f"You typed in {index - 1} different words")
    else:
        list.append(word)
        index += 1