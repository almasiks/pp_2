
def is_above_5_5(movie):
    return movie["imdb"] > 5.5

def movies_above_5_5(movies):
    return [m for m in movies if m["imdb"] > 5.5]

def movies_by_category(movies, category):
    return [m for m in movies if m["category"].lower() == category.lower()]

def average_imdb(movies):
    if not movies:
        return 0
    return sum(m["imdb"] for m in movies) / len(movies)

def average_imdb_by_category(movies, category):
    filtered = movies_by_category(movies, category)
    return average_imdb(filtered)
