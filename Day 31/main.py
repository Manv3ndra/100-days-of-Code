import requests
from bs4 import BeautifulSoup

response = requests.get("https://news.ycombinator.com")
soup = BeautifulSoup(response.content, "html.parser")

articles = soup.find_all("a", class_= "titlelink")
article_name = []
article_links = []
article_upvotes = []

for article_tag in articles:
    text = article_tag.getText()
    article_name.append(text)
    links = article_tag.get("href")
    article_links.append(links)

upvotes = soup.find_all("span", class_= "score")
for i in upvotes:
    votes = i.getText()
    int_votes = votes.split()
    article_upvotes.append(int(int_votes[0]))

max_index = article_upvotes.index(max(article_upvotes))
print(article_name[max_index])
print(article_links[max_index])
print(article_upvotes[max_index])