#1
number = input("Please type in a number:")
output = int(number)
print(f"{number} times 5 is {output*5}")

#2
name = input("What is your name?")
year = input("Which year were you born?")
result = 2021-int(year)
print(f"Hi {name}, you will be {result} years old at the end of the year 2021")

#3
day = input("How many days?")
result = int(day)*24*60*60
print(f"Seconds in that many days: {result}")

#4
number1 = int(input("Please type in the first number: "))
number2 = int(input("Please type in the second number: "))
number3 = int(input("Please type in the third number: "))
product = number1 * number2 * number3
print(f"The product is {product}")

#5
n1 = input("Number 1:")
n2 = input("Number 2:")
sum = int(n1)+int(n2)
product = int(n1)*int(n2)
print(f"The sum of the numbers: {sum}")
print(f"The product of the numbers: {product}")

#6
n1 = input("Number 1:")
n2 = input("Number 2:")
n3 = input("Number 3:")
n4 = input("Number 4:")
sum = int(n1)+int(n2)+int(n3)+int(n4)
mean = sum/4
print(f"The sum of the numbers is {sum} and the mean is {mean}")

#7
many = int(input("How many times a week do you eat at the student cafeteria? "))
pris = float(input("The price of a typical student lunch? "))
week = float(input("How much money do you spend on groceries in a week? "))
weekly = many * pris + week
daily = weekly / 7
print("\nAverage food expenditure:")
print(f"Daily: {daily} euros")
print(f"Weekly: {weekly} euros")

#8
many = int(input("How many students on the course? "))
size = int(input("Desired group size? "))
group = many // size
if many % size != 0:
    group += 1
print(f"Number of groups formed: {group}")