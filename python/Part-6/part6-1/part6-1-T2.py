def read_fruits():
    fruits = {}
    with open("fruits.csv") as file:
        for line in file:
            name, price = line.strip().split(";")
            fruits[name] = float(price)
    return fruits