def line(n, ch):
    if len(ch) == 1:
        print(n*ch)
    elif ch == "":
        print(n*"*")
    else:
        print(n*ch[0])
def shape(s1, c1, s2, c2):
            side = 1
            h = 1
            while s1 >= side:
                line(side, c1)
                side += 1
            while h <= s2:
                line(s1, c2)
                h += 1

if __name__ == "__main__":
    shape(5, "x", 3, "*")