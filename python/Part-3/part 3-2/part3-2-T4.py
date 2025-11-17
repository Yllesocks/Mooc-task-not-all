string = input("Please type in a string:")
second_char= string[1]
second_last_char= string[-2]

if second_char == second_last_char:
    print(f"The second and the second to last characters are {second_char}")
else:
    print("The second and the second to last characters are different")