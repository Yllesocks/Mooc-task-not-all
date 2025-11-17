#1
number = int(input("Please type in a number:"))

if number > 100:
  print("The number was greater than one hundred")
  print("Now its value has decreased by one hundred")
  number = number - 100
  print(f"Its value is now {number}")

print(f"{number} must be my lucky number!")
print("Have a nice day!")

#2
word = input("Please type in a word:")
if len(word) > 1:
    print(f"There are {len(word)} letters in the word {word}")
print("Thank you!")

#3
number = float(input("Please type in a number:"))
print("Integer part:", int(number))
print("Decimal part:", number-int(number))