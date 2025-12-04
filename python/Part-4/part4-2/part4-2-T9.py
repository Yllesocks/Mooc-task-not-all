def same_chars(a, b, c):
    if c >= len(a) or b >= len(a):
        return False
    elif a[b] == a[c]:
        return True
    else:
        return False

if __name__ == "__main__":
    print(same_chars("abc", 0, 3))