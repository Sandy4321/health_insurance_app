import requests
from bs4 import BeautifulSoup

url = 'http://www.politico.com/2014-election/general/results/map/senate#.WAbEQ5MrKHo'
resp = requests.get(url)
soup = BeautifulSoup(resp.text,'html')

soup = soup.find('div', {'class': 'content-alpha'})
hrefs = []

for s in soup.findAll('article', {'class': 'timeline-group'}):
    hrefs.append(s.find(text='Detailed Results').parent.findParent('a')['href'])

for h in hrefs:
    url = h[1]
    state = h[0]
    state_dict[state] = {}
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text,'html')
    
    soup = soup.find('div', {'class': 'content-alpha'})

    for s in soup.findAll('article', {'class': 'results-group'}):
        county = s.find('div', {'class':'title'}).text
        state_dict[state][county] = []
        for r in s.find('table', {'class': 'results-table'}).findAll('tr'):
            l = []
            l.append(r['class'][0].split('-')[1])
            l.append(r.find('span', {'class':'number'}).text)
            l.append(r.find('td', {'class':'results-popular'}).text)
            state_dict[state][county].append(l)

    sleep(.1)
