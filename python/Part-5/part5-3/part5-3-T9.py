def find_movies(database: list, search_term: str):
    results = []
    search_term = search_term.lower()

    for movie in database:
        if search_term in movie["name"].lower():
            results.append(movie)

    return results
