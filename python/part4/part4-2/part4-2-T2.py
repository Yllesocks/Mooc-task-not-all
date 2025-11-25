def line(n, ch):
    if len(ch) == 1:
        print(n*ch)
    elif ch == "":
        print(n*"*")
    else:
        print(n*ch[0])

def box_of_hashes(h):
    while h > 0:
        line(10, "#")
        h -= 1

if __name__ == "__main__":
    box_of_hashes(5)