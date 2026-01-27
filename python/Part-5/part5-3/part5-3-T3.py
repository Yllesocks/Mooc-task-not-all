def histogram(string: str):
    counts = {}

    for char in string:
        counts[char] = counts.get(char, 0) + 1

    for char in counts:
        print(f"{char} {'*' * counts[char]}")
