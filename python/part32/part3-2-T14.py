word = input("Please type in a word:")
character = input("Please type in a character:")

index = word.find(character)

while True:
    output = word[index:index + 3]
    if len(word) == 0 or len(output) != 3:
        break
    elif output.find(character) == 0:
        print(output)
    word = word[1:]
