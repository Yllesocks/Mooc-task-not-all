import heapq

def all_the_longest(my_list: list):
    i = max(map(len, my_list))
    list = [word for word in my_list if len(word) == i]
    return list


if __name__ == "__main__":
    my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]
    result  = all_the_longest(my_list)
    print(result)
