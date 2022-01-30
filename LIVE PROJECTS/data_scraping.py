import requests
from bs4 import BeautifulSoup
import html5lib

URL = "https://data.stackexchange.com/stackoverflow/queries?order_by=everything"

stack = requests.get(URL)

soup = BeautifulSoup(stack.content, 'html5lib')

result = soup.find(id="mainbar")

view = result.find_all('div', class_="views")

views = []

views.append(view.text)

print(views.prettify())