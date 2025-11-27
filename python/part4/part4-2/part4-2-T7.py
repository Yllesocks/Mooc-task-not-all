def spruce(n):
    index = 1
    print("a spruce!")
    while index <= n:
        side = n - index
        print(" " * side + "*" *(2 * index - 1))
        index += 1
    print(" " * (n-1) + "*")

if __name__ == "__main__":
    spruce(5)