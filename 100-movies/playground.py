# from bs4 import BeautifulSoup

# with open('website.html') as file:
#     content = file.read()

# soup = BeautifulSoup(content, 'html.parser')
# print(soup.title)
# print(soup.h1)
# print(soup.title.name)
# print(soup.title.string)

# print('#####################')
# # print(soup.prettify())
# all_anchor_tags = soup.find_all(name='a')
# for atag in all_anchor_tags:
#     # print(atag.getText())
#     print(atag.get('href'))

# # heading = soup.find(name='h1', id='name')
# headings = soup.select('.heading')
# print(headings)

# section_heading = soup.find(name='h3', class_='heading')
# print(section_heading)
# print(section_heading.getText())

# company_url = soup.select_one(selector='p a')
# print(company_url)

# name = soup.select_one('#name')
# print(name)

from bs4 import BeautifulSoup
import requests

response = requests.get('https://news.ycombinator.com/')
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, 'html.parser')
# print(soup.title)
a_tags = soup.select(selector='.titleline a')
# for tag in a_tags:
#     print(tag.getText())
print(a_tags[6].getText())