def no_shouting(list):
    new_list = []
    index = 0
    for i in list:
        if list[index].isupper() == False:
            new_list.append(list[index])
        index += 1
    return new_list

if __name__ == "__main__":
    my_list = ["ABC", "def", "UPPER", "ANOTHERUPPER", "lower", "another lower", "Capitalized"]
    pruned_list = no_shouting(my_list)
    print(pruned_list)
