from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import os, ssl

if (not os.environ.get('PYTHONHTTPSVERIFY', '') and getattr(ssl, '_create_unverified_context', None)):
    ssl._create_default_https_context = ssl._create_unverified_context

url_to_scrape = Request('https://rowingmanager.com/regattas/5212/results' , headers={'User-Agent': 'Mozilla/5.0'})

request_page = urlopen(url_to_scrape)
page_html = request_page.read()
request_page.close()

html_soup = BeautifulSoup(page_html, 'html.parser')

res = html_soup.find_all('td', class_='rm_nowrap')

# res2 = html_soup.find_all('tbody', class_='rm_nowrap')

print(res)

# filename = 'results.csv'
# f = open(filename, 'w')

# for club in res:
#     data = club.find('div')
#     f.write(data)

# f.close()