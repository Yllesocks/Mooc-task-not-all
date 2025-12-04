def palindromes(a: str):
    if a == a[::-1]:
        return True
    else:
        return False

while True:
    a = input("Please type in a palindrome:")
    if palindromes(a) == False:
        print("that wasn't a palindrome")
    else:
        print(f"{a} is a palindrome!")
        break