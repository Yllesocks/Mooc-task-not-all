word = input("Please type in a string:")
CHs = input("Please type in a substring:")
first_index = word.find(CHs)

if first_index == -1:
    print("The substring does not occur twice in the string.")
else:
    second_index = word.find(CHs, first_index + len(CHs))
    if second_index != -1:
        print(f"The second occurrence of the substring is at index {second_index}.")
    else:
        print("The substring does not occur twice in the string.")