#1
old = int(input("How old are you?"))
if old >= 18:
    print("You are of age!")
else:
    print("You are not of age!")
#2
num1 = int(input("Please type in the first number:"))
num2 = int(input("Please type in the another number:"))

if num1 > num2:
    print(f"The greater number was: {num1} ")
elif num2 > num1:
    print(f"The greater number was: {num2} ")
else:
    print("The numbers are equal!")

#3
print("Person 1:")
name1 = input("Name:")
age1 = int(input("Age:"))
print("Person 2:")
name2 = input("Name:")
age2 = int(input("Age:"))

if age1 > age2:
    print(f"The elder is {name1}")
elif age2 > age1:
    print(f"The elder is {name2}")
else:
    print(f"{name1} and {name2} are the same age")

#4
word1 = input("Please type in the first word: ")
word2 = input("Please type in the second word: ")

if word1 > word2:
    print(f"{word1} comes alphabetically last.")
elif word2 > word1:
    print(f"{word2} comes alphabetically last.")
else:
    print("You gave the same word twice.")