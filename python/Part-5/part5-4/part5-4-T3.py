def older_people(people: list, year: int):
    result = []

    for name, birth_year in people:
        if birth_year < year:
            result.append(name)

    return result
