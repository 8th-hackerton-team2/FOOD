from bs4 import BeautifulSoup
import requests

class Restaurant:
	def __init__(self, name, detail_id, img_thumb, content):
		self.name = name
		self.detail_id = detail_id
		self.img_thumb = img_thumb
		self.content = content
		self.menu = None
		self.address = None
		self.tel = None

url = 'https://store.naver.com/restaurants/list?'
params = {'menu':'한식', 'page':1, 'query':'성수동%20맛'}
restaurant_url = requests.get(url,params)
html = restaurant_url.text
soup = BeautifulSoup(html, 'lxml')

restaurant_list = soup.select_one('ul > li')

