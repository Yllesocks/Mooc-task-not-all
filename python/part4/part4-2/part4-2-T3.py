def line(n, ch):
    if len(ch) == 1:
        print(n*ch)
    elif ch == "":
        print(n*"*")
    else:
        print(n*ch[0])

def square_of_hashes(size):
    side = size
    while size > 0:
        line(side, "#")
        size -= 1

if __name__ == "__main__":
    square_of_hashes(5)