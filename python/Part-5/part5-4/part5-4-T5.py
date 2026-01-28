layers = int(input("Layers: "))

size = 2 * layers - 1

for row in range(size):
    for col in range(size):
        distance = min(row, col, size - 1 - row, size - 1 - col)
        letter = chr(ord('A') + layers - 1 - distance)
        print(letter, end="")
    print()
