def largest():
    with open("numbers.txt") as file:
        numbers = [int(line.strip()) for line in file]
    return max(numbers)