def everything_reversed(result):
    return [s[::-1] for s in my_list[::-1]]

if __name__ == "__main__":
    my_list = ["Hi", "there", "example", "one more"]
    new_list = everything_reversed(my_list)
    print(new_list)