import requests
from bs4 import BeautifulSoup

response = requests.get("https://www.empireonline.com/movies/features/best-movies-2/")
soup = BeautifulSoup(response.text, "html.parser")

movies = []

movie_name = soup.find_all(name="h3", class_="jsx-4245974604")
for i in movie_name:
    name = i.get_text()
    movies.append(name)

print(movies)