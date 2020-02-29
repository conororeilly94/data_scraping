import requests # Downloads intial HTML
from bs4 import BeautifulSoup
import pprint

res = requests.get('https://news.ycombinator.com/front')
res2 = requests.get('https://news.ycombinator.com/front?day=2020-02-28&p=2')
soup = BeautifulSoup(res.text, 'html.parser')
soup2 = BeautifulSoup(res2.text, 'html.parser')

# print(soup.title) #content, 'a' etc to find certain requests
# print(soup.find(id='12345'))
# print(soup.select('#score_22450298'))
# print(soup.select('.storylink')[0])

links = soup.select('.storylink')
subtext = soup.select('.subtext')
links2 = soup2.select('.storylink')
subtext2 = soup2.select('.subtext')

mega_links = links + links2
mega_subtext = subtext + subtext2

def sort_stories_by_votes(hnlist): # Must tell how to sort by title, link etc
	return sorted(hnlist, key= lambda k:k['votes'], reverse=True)

#print(votes[0])
# print(votes[0].get('id'))

def create_custom_hn(links, subtext):
	hn = []
	for idx, item in enumerate(links):
		title = item.getText()
		href = item.get('href', None)
		vote = subtext[idx].select('.score')
		if len(vote):
			points = int(vote[0].getText().replace(' points', ''))
			# Points over a 100
			if points > 200:
				hn.append({'title': title, 'link': href, 'votes': points})
	return sort_stories_by_votes(hn)

pprint.pprint(create_custom_hn(mega_links, mega_subtext))