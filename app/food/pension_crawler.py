import requests
from bs4 import BeautifulSoup
request = requests.get("http://www.yapen.co.kr")

response = request.text

soup = BeautifulSoup(response, 'lxml')

class Yanolja:
    def __init__(self, name, img, price ):
        self.name = name
        self.img = img
        self.price =price
    def __repr__(self):
        return f'{self.img} {self.name}, {self.price}\n'

title = soup.select('div.pensionName')
img_file = soup.select('img.pensionImg')
price=soup.select('div.price')
title_list = []
img_file_list= []
price_list = []
for i in title:
    title_list.append(i.get_text())
for i in img_file:
    img_file_list.append(i.get('src'))
for i in price:
    price_list.append(i.get_text())

ya = []
for i in range(len(title_list)):
	ya.append(Yanolja(name=title_list[i], price=price_list[i], img=img_file_list[i]))
print(ya)