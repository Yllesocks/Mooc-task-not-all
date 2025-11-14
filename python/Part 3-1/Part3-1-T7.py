limit = int(input("Limit: "))
number = 1
sum = 0
calculation = ""
while sum < limit:
    sum += number
    calculation += str(number)
    if sum < limit:
        calculation += " + "
    number += 1
print(f"The consecutive sum: {calculation} = {sum}")