import requests
from bs4 import BeautifulSoup

headers = {'User-Agent' : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 OPR/82.0.4227.50"}

response = requests.get(url="https://www.timeout.com/film/best-movies-of-all-time", headers=headers)
soup = BeautifulSoup(response.content, "html.parser")

movies = []

movie_data = soup.find_all("h3", class_="_h3_cuogz_1")
for movie in movie_data:
    name = movie.get_text().replace('''\xa0'''," ").split()
    movies.append(name)

movies.remove(movies[-1])

all_movies = []
for i in range(0,100):
    movie_name_all = movies[i][1:len(movies[i])]
    movie_name = ""
    for j in movie_name_all[0:len(movie_name_all)-1]:
        movie_name += j + " "
        final_name = (str(i+1)+". ") + movie_name
    all_movies.append(final_name.rstrip())

with open("100_Greatest_Movies.txt", "a") as f:
    for item in all_movies:
        f.write(item + "\n")