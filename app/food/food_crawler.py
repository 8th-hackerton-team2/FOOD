from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.Chrome('/Users/apple/Downloads/chromedriver')

driver.implicitly_wait(3)

response = driver.get('https://search.daum.net/search?q=성수동+한식')
html = response.text

soup = BeautifulSoup(html, 'lxml')

name = soup.select('a.fn_tit')
for i in name:
    print(i.get_text())
