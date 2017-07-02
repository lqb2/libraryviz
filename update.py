import requests
from bs4 import BeautifulSoup
from jinja2 import Template



response = requests.get(
	'https://www.goodreads.com/review/list/61877628-lawrence?order=d&per_page=100&shelf=read&sort=date_read')
html = response.content.decode('utf-8')

soup = BeautifulSoup(html, 'html.parser')

def fixImageURL(anchortag):
	img = anchortag.img
	# grab src attribute of image
	imgsrc = img['src']
	# break line up by /
	chunks = imgsrc.split('/')
	# replacing the s with an l in the 2nd to last in chunks 
	chunks[-2] = chunks[-2].replace('s','l')
	# put the list back together
	result = "/".join(chunks)
	img['src'] = result

def fixBookURL(anchortag):
	href = anchortag['href']
	fixedURL = "https://www.goodreads.com" + href
	anchortag['href'] = fixedURL

	# one line version of the above code
	# anchortag['href'] = "https://www.goodreads.com" + anchortag['href']

# images = soup.find_all("img")
# print(images)

bookDivs = soup.find_all("div", { "data-resource-type" : "Book" })

# print(bookDivs)
# print(bookDivs[0].contents[1])

anchortags = []
for div in bookDivs:
	fixImageURL(div.a)
	fixBookURL(div.a)
	anchortags.append(div.a)

# print(anchortags)

with open('template.html.jinja') as template_file:
	template = Template(template_file.read())


rendered_html = template.render(
	anchortags=anchortags, username='Lawrence Q. Barriner II')

with open('index.html', "w") as outputFile:
	outputFile.write(rendered_html)

# print(rendered_html)

# print(anchortags[0])

# print(anchortags[0].img['src'])
# print img['src']

# fixImageURL(anchortags[0])

# print(anchortags[0])


