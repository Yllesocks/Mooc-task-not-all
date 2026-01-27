def factorials(n: int):
    result = {}
    current = 1

    for i in range(1, n + 1):
        current *= i
        result[i] = current

    return result
