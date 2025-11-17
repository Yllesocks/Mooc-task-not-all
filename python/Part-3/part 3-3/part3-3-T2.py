sentence = input("Please type in a sentence:")

sentence = " " + sentence
index = 1

while index <= len(sentence):
    if sentence[index -1] == " " and sentence[index] != " ":
        print(sentence[index])
    index += 1
    