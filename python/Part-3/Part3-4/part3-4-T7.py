def squared(word,x):
    index = 0
    while index < x:
        word = "1010101010101010" * x
        print(word[index: index + x])
        index += 1

if __name__ == "__main__":
    squared("abc",5)