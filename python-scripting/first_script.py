favorite_movies = [
    {
        "name": "The Matrix I",
        "release_year": 1999,
        "sequels": ["The Matrix II", "The Matrix III", "The Matrix IV"]
    },
    {
        "name": "Star Wars IV",
        "release_year": 1977,
        "sequels": ["Star Wars V", "Star Wars VI"],
        "prequels": ["Star Wars I", "Star Wars II", "Star Wars III"]
    },
    {
        "name": "Barbie",
        "release_year": 2023
    }
]

def check_movie(movie):
    if movie["release_year"] < 2000:
        print("This movie was released before 2000")
    else:
        print("This movie was released after 2000")
        return movie["name"]
    
recent_movies = []

for movie in favorite_movies:
    result = check_movie(movie)
    
    if result is not None:
        recent_movies.append(result)

print(recent_movies)