import requests # Downloads intial HTML
from bs4 import BeautifulSoup

res = requests.get('https://news.ycombinator.com/newest')
soup = BeautifulSoup(res.text, 'html.parser')
#print(soup.title) #content, 'a' etc to find certain requests
# print(soup.find(id='12345'))
print(soup.select('#score_22450298'))