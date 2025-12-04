def even_numbers(my_list):
    new_list = []
    i = 0
    for n in my_list:
        if my_list[i] % 2 == 0:
            new_list.append(my_list[i])
        i += 1
    return new_list

if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5]
    new_list = even_numbers(my_list)
    print("original", my_list)
    print("new", new_list)