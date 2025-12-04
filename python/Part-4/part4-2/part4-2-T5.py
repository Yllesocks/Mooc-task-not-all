def line(n, ch):
    if len(ch) == 1:
        print(n*ch)
    elif ch == "":
        print(n*"*")
    else:
        print(n*ch[0])

def triangle(size):
        side = 1
        while size >= side:
            line(side, "#")
            side += 1

if __name__ == "__main__":
    triangle(5)
