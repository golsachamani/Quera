
n = int(input())

fixed_movies = []

for _ in range(n):
    movie = input()
    fixed_movie = movie.title()
    fixed_movies.append(fixed_movie)


for movie in fixed_movies:
    print(movie)
