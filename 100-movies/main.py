from bs4 import BeautifulSoup
import requests

URL = 'https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/'

response = requests.get(URL)
web_page = response.text

soup= BeautifulSoup(web_page, 'html.parser')
titles = soup.select('h3.title')

# print(len(titles))
# print(titles[0])
titles_list = [titles[0].getText()]

for title in titles:
    titles_list.insert(0, title.getText())

titles_list.pop()

with open('movies.txt', mode='w') as file:
    for movie in titles_list:
        file.write(f"{movie}\n")
