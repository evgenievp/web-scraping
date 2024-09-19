from bs4 import BeautifulSoup
import requests

url = 'https://books.toscrape.com/catalogue/category/books/philosophy_7/index.html'
page = requests.get(url).text
soup = BeautifulSoup(page, 'html.parser')

container = soup.find_all('article', 'product_pod')
data = ''
with open("philsoophy books.txt", 'w') as file:
    for li in container:
        text = li.text.replace("\n", "|")
        ready_text = text.strip("|")
        data += f"{ready_text}\n"
    file.write(data)
