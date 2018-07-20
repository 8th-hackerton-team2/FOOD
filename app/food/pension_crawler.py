import re

import requests
from bs4 import BeautifulSoup
from .models import Pension


def pension_crawler():
    request = requests.get("http://www.yapen.co.kr")

    response = request.text

    soup = BeautifulSoup(response, 'lxml')

    title = soup.select('div.pensionName')
    img_file = soup.select('img.pensionImg')
    price=soup.select('div.price')
    title_list = []
    img_file_list= []
    price_list = []
    num_list = []
    for i in title:
        title_list.append(i.get_text())
    for i in img_file:
        img_file_list.append(i.get('src'))
    for i in price:
        price_list.append(i.get_text())

    for i in img_file:
        src = i.get('src')

        list = re.split('/', src)

        num_list.append(int(list[5]))

    for i in range(len(img_file_list)):
        name= title_list[i]
        photo = img_file_list[i]
        price = price_list[i]
        num = num_list[i]

        Pension.objects.get_or_create(
            name=name,
            photo=photo,
            price=price,
            pldx=num,
        )


