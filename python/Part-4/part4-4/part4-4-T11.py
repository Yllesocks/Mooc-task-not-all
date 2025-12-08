def shortest(strings):
    shortest_str = strings[0]
    for s in strings[1:]:
        if len(s) < len(shortest_str):
            shortest_str = s
    return shortest_str


if __name__ == "__main__":
    my_list = ["first", "second", "fourth", "eleventh"]
    result  = shortest(my_list)
    print(result)
