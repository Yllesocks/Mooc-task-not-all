#1
name = "Tim Tester"
age = 20
skill1 = "python"
level1 = "beginner"
skill2 = "java"
level2 = "veteran"
skill3 = "programming"
level3 = "semiprofessional"
lower = 2000
upper = 3000

print("my name is", name + ", I am",age, "years old")
print()
print("my skills are")
print(" - " + skill1 + " (" + level1 + ")")
print(" - " + skill2 + " (" + level2 + ")")
print(" - " + skill3 + " (" + level3 + ")")
print( )
print(f"I am looking for a job with a salary of {lower}-{upper} euros per month")

#2
x = 27
y = 15
plus = (x+y) 
minus = (x-y)
gånger = (x*y) 
div = (x/y)
print(f"27 + 15 = {plus}")
print(f"27 - 15 = {minus}")
print(f"27 * 15 = {gånger}")
print(f"27 / 15 = {div}")

#3
print(5 , end="")
print(" + " , end="")
print(8 , end="")
print(" - " , end="")
print(4 , end="")
print(" = " , end="")
print(5 + 8 - 4)