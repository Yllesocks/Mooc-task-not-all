#1
while True:
    print("hi")
    ans = input("Shall we continue?")
    if ans == "no":
        break
        
print("okay then")

#2
from math import sqrt
while True:
    number = int(input("Please type in a number: "))

    if number == 0:
        print("Exiting...")
        break
    elif number < 0:
        print("Invalid number")
    else:
        print(sqrt(number))

#3
number = 5
print("Countdown!")
while number > 0:
    print(number)
    number = number - 1

print("Now!")

#4
password = input("Password: ")
repeat = input("Repeat password: ")

while repeat != password:
    print("They do not match!")
    repeat = input("Repeat password: ")

print("User account created!")

#5
correct_pin = "4321"
attempts = 0

while True:
    pin = input("PIN: ")
    attempts += 1
    if pin == correct_pin:
        if attempts == 1:
            print("Correct! It only took you one single attempt!")
        else:
            print(f"Correct! It took you {attempts} attempts")
        break
    else:
        print("Wrong")

#6
year = int(input("Year: "))

def is_leap(y):
    return (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0)

next_year = year + 1
while not is_leap(next_year):
    next_year += 1

print(f"The next leap year after {year} is {next_year}")

#7
story = ""
previous_word = ""

while True:
    word = input("Please type in a word: ")
    if word == "end" or word == previous_word:
        break
    story += word + " "
    previous_word = word

print(story)

#8
print("Please type in integer numbers. Type in 0 to finish.")
how_many_numbers = 0
sum = 0
mean = 0
p_num = 0
n_num = 0

while True:
    number = int(input("Number:"))

    if number > 0:
        p_num += 1
    elif number < 0:
        n_num += 1

    how_many_numbers += 1
    sum += number
    if number == 0:
        break

mean = sum / (how_many_numbers - 1)
print("... the program asks for numbers")
print(f"Numbers typed in {how_many_numbers - 1}")
print(f"The sum of the numbers is {sum}")
print(f"The mean of the numbers is {mean}")
print(f"Positive numbers {p_num}")
print(f"Negative numbers {n_num}")