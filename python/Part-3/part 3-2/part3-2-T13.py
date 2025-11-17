input_word = input("Please type in a word:")
search_words = input("Please type in a character:")

index = input_word.find(search_words)
output = input_word[index:index + 3]
if len(output) != 3:
    print("")
elif len(output) == 3:
    print(output)
else:
    print("")