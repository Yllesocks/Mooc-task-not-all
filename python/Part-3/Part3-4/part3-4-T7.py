def squared(word,x):
    index = 0
    row = ""
    while index < x * x:
        if index > 0 and index % x == 0:
            print(row)
            row = ""
        row += word[index % len(word)]
        index += 1
    print(row)

if __name__ == "__main__":
    squared("ab", 3)