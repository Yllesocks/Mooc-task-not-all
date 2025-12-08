def length_of_longest(length):
    longest = 0
    for s in length:
        if len(s) > longest:
            longest = len(s)
    return longest


if __name__ == "__main__":
    my_list = ["first", "second", "fourth", "eleventh"]
    length = length_of_longest(my_list)
    print(length)
