def line(n, ch):
    if len(ch) == 1:
        print(n*ch)
    elif ch == "":
        print(n*"*")
    else:
        print(n*ch[0])
if __name__ == "__main__":
    line(5, "")