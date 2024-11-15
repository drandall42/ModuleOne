class film():
    def __init__(self, title, genre, length, rating):
        self.title = title
        self.genre = genre
        self.length = length
        self.rating = rating

def printFilm(movie):
    print(f"{movie.title}, {movie.genre}, {movie.legnth}, {movie.rating}")