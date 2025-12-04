def mean(my_list) -> float:
    return sum(my_list) / len(my_list)

if __name__ == "__main__":
    my_list = [1, 3, 67, 7, 4, 23, 1, 5, 7, 4]
    result = mean(my_list)
    print(result)