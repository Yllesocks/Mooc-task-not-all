#1
age = int(input("What is your age?"))
if age >= 0 and age < 5:
    print("I suspect you can't write quite yet...")
elif age < 0:
    print("That must be a mistake")
else:
    print(f"Ok, you're {age} years old")

#2
name = input("Please type in your name:")

if name == "Huey" or name == "Dewey" or name == "Louie":
    print("I think you might be one of Donald Duck's nephews.")
elif name == "Morty" or name == "Ferdie":
    print("I think you might be one of Mickey Mouse's nephews.")
else:
    print("You're not a nephew of any character I know of.")

#3
points = int(input("How many points [0-100]:"))
if points < 0 or points > 100:
    print("Grade: impossible!")
elif points < 50 and points > 0:
    print("Grade: fail")
elif points <= 59 and points >= 50:
    print("Grade: 1")
elif points <= 69 and points >= 60:
    print("Grade: 2")
elif points <= 79 and points >= 70:
    print("Grade: 3")
elif points <= 89 and points >= 80:
    print("Grade: 4")
elif points <= 100 and points >= 90:
    print("Grade: 5")

#4
number = int(input("Please type in a number: "))
if number % 3 == 0 and number % 5 == 0:
    print("FizzBuzz")
elif number % 3 == 0:
    print("Fizz")
elif number % 5 == 0:
    print("Buzz")

#5
year = int(input("Please type in a year:"))

if year % 100 == 0 and year % 400 == 0:
    print("That year is a leap year.")
elif year % 100 == 0:
    print("That year is not a leap year.")
elif year % 4 == 0:
    print("That year is a leap year.")
else:
    print("That year is not a leap year.")

#6
letter1 = input("1st letter: ")
letter2 = input("2nd letter: ")
letter3 = input("3rd letter: ")
letters = [letter1, letter2, letter3]
letters.sort()
print("The letter in the middle is " + letters[1])

#7
value = int(input("Value of gift: "))
tax = 0

if value < 5000:
    tax = 0
elif value < 25000:
    tax = 100 + (value - 5000) * 0.08
elif value < 55000:
    tax = 1700 + (value - 25000) * 0.10
elif value < 200000:
    tax = 4700 + (value - 55000) * 0.12
elif value < 1000000:
    tax = 22100 + (value - 200000) * 0.15
else:
    tax = 142100 + (value - 1000000) * 0.17

if tax == 0:
    print("No tax!")
else:
    print(f"Amount of tax: {tax:.0f} euros")