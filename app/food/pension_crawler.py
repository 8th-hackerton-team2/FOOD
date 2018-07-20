import re
from urllib import parse

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

def pension_detail_cralwer(ypIdx):

    params = {
        'ypIdx': ypIdx
    }

    url = "http://www.yapen.co.kr/details?" + parse.urlencode(params)

    request = requests.get(url)
    response = request.text
    soup = BeautifulSoup(response, 'lxml')

    name_root = soup.select('div.wrap_1000')
    name = name_root[0].select('h3')[0].get_text()

    table = soup.select('table.pensionTbl')
    trs = table[0].select('tr')
    tds = trs[0].select('td')
    address = tds[0].get_text()

    tds2 = trs[1].select('td')
    check_in_out = tds2[0].select('span')
    check_in = check_in_out[0].get_text()
    check_out = check_in_out[1].get_text()

    td3 = trs[3].select('td')
    number_tags = td3[0].select('span')
    room = number_tags[0].get_text()

    td4 = trs[4].select('td')
    infos = td4[0].select('p')
    info_result = ''
    for info in infos:
        info_result = info_result + '\n' + info.get_text() + '\n'

    td5 = trs[5].select('td')
    lis = td5[0].select('li')
    theme_result = ''
    for li in lis:
        theme_result = theme_result + '\n' + li.get_text() + '\n'


    pension =Pension.objects.filter(name=name)[0]
    pension.address=address
    pension.check_in= check_in
    pension.check_out = check_out
    pension.room = room
    pension.info = info_result
    pension.theme = theme_result
    pension.save()

    return pension

