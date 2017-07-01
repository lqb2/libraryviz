import requests

response = requests.get(
	'http://www.goodreads.com/review/list/61877628-lawrence?shelf=read')
html = response.content.encode('utf-8')

from bs4 import BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')
