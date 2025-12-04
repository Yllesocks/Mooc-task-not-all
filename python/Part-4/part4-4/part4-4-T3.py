def list_of_stars(i):
    index = 0
    for index in range(len(i)):
        print(i[index]* "*")
        index += 1 

if __name__ == "__main__":
    list_of_stars([3, 7, 1, 1, 2])