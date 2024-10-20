from bs4 import BeautifulSoup
import requests

url = 'https://zodiac.dir.bg/sign/lav/dneven-horoskop'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')
container = soup.find_all('div', 'article-body horoscope')
res = ''
stars = ''
for el in container:
    ul = el.find('ul')
    stars += ul.text
    e = el.find('p')
    res += e.text

res = res.replace(".", '.\n')
stars = stars.replace("\n", "")
print(res)
print(stars)