def no_vowels(string):
    vowels = "aeiou"
    result = ""
    for ch in string:
        if ch not in vowels:
            result += ch
    return result

if __name__ == "__main__":
    string = "this is an example"
    print(no_vowels(string))