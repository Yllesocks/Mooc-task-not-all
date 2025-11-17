#1
num = int(input("Please type in a number:"))
if num == 1984:
    print("Orwell")

#2
num = int(input("Please type in a number:"))
if num < 0:
    print(f"The absolute value of this number is {num*-1}")
if num > 0:
    print(f"The absolute value of this number is {num}")
if num == 0:
    print(f"The absolute value of this number is {num}")

#3
name = input("Please tell me your name:")
if name == "Jerry":
    print("Next please!")

if name != "Jerry":
    many = int(input("How many portions of soup?"))
    cost = float(5.90 * many)
    print(f"The total cost is {cost}")
    print("Next please!")

#4
num = int(input("Please type in a number: "))
if num <1000:
    print("This number is smaller than 1000")
if num <100:
    print("This number is smaller than 100")
if num <10:
    print("This number is smaller than 10")
print("Thank you!")    

#5
num1 = int(input("Number 1:"))
num2 = int(input("Number 2:"))
op = input("Operation:")
if op == "add":
    print(f"{num1} + {num2} = {num1+num2}")
if op == "multiply":
    print(f"{num1} * {num2} = {num1*num2}")
if op == "subtract":
    print(f"{num1} - {num2} = {num1-num2}")

#6
tempf = int(input("Please type in a temperature (F):"))
tempc = ((tempf - 32)*5)/9
print(f"{tempf} degrees Fahrenheit equals {tempc} degrees Celsius")
if tempc < 0:
    print("Brr! It's cold in here!")

#7
wage = float(input("Hourly wage:"))
hours = float(input("Hours worked:"))
day = input("Day of the week:")
if day == "Sunday":
    print(f"Daily wages: {(wage*hours)*2} euros")
if day != "Sunday":
    print(f"Daily wages: {wage*hours} euros")

#8
points = int(input("How many points are on your card? "))
if points < 100:
    points *= 1.1
    print("Your bonus is 10 %")
else:
    points *= 1.15
    print("Your bonus is 15 %")
print(f"You now have {points} points")

#9
print("What is the weather forecast for tomorrow?")
temperature = int(input("Temperature: "))
rain = input("Will it rain (yes/no): ")
print("Wear jeans and a T-shirt")
if temperature <= 20:
    print("I recommend a jumper as well")

if temperature <= 10:
    print("Take a jacket with you")
if temperature <= 5:
    print("Make it a warm coat, actually")
    print("I think gloves are in order")
if rain == "yes":
    print("Don't forget your umbrella!")

#10
from math import sqrt
a = int(input("Value of a:"))
b = int(input("Value of b:"))
c = int(input("Value of c:"))
x1=(-b + sqrt(b**2 - 4*a*c))/(2*a)
x2=(-b - sqrt(b**2 - 4*a*c))/(2*a)
print(f"The roots are {x1} and {x2}")