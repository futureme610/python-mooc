def find_movies(database: list, search_term: str):
    #formulate a new list which contains only the movies whose title
    #includes the word searched for

    search_database = []
    for movie in database:
        if search_term.lower() in movie["name"].lower():
            if movie not in search_database:
                search_database.append(movie)
    
    return search_database

if __name__ == "__main__":
    database = [{"name": "Gone with the Python", "director": "Victor Pything", "year": 2017, "runtime": 116},
    {"name": "Pythons on a Plane", "director": "Renny Pytholin", "year": 2001, "runtime": 94},
    {"name": "Dawn of the Dead Programmers", "director": "M. Night Python", "year": 2011, "runtime": 101}]

    my_movies = find_movies(database, "python")
    print(my_movies)