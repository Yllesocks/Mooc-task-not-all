def list_sum(a, b):
    list_sum = []
    i = 0
    for n in a:
        list_sum.append(a[i] + b[i])
        i += 1
    return list_sum

if __name__ == "__main__":
    a = [1, 2, 3]
    b = [7, 8, 9]
    print(list_sum(a, b)) # [8, 10, 12]