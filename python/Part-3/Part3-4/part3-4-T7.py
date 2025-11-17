def squared(word, x):
    index = 0
    while index < x:
        out = word * x
        print(out[index: index + x])
        index += 1

if __name__ == "__main__":
    squared("abc", 5)