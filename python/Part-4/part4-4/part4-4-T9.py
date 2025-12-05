def distinct_numbers(numbers):
    return sorted(set(numbers))

if __name__ == "__main__":
    list = [1, 2, 3, 3, 4, 3, 4 ]
    print(distinct_numbers(list))