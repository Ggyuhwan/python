from bs4 import BeautifulSoup
import requests
import csv
import re

def fn_get_musinsa(page):
    url = 'https://www.musinsa.com/mz/community?p='+ str(page)
    res = requests.get(url)
    soup = BeautifulSoup(res.content,'html.parser')
    uls = soup.find('ul', class_='ul-col')
    lis = uls.find_all('li')
    arr = []
    for i, li in enumerate(lis):
        if i > 1:
            print(li)
            cate = li.find('span', class_='colName').text
            date = li.find('span', class_='colDate').text
            hit = li.find('span', class_='colHit').text
            arr.append([cate, date. hit])
    return arr
print(fn_get_musinsa(1))
