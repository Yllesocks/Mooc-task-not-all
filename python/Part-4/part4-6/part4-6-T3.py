def most_common_character(string: str):
    new_string = string[0]
    for character in string:
        if string.count(character) > string.count(new_string):
            new_string = character
    return new_string

if __name__ == "__main__":
    first_string = "abcdbde"
    print(most_common_character(first_string))
    second_string = "exemplaryelementary"
    print(most_common_character(second_string))