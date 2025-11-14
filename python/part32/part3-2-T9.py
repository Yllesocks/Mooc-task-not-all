word = input("Please type in a string:")
width = 30
padding = (width - 2 - len(word)) // 2
left_padding = padding
right_padding = width - 2 - len(word) - left_padding
print("*" * 30)
print("*" + " " * left_padding + word + " " * right_padding + "*")
print("*" * 30)
