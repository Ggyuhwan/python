from bs4 import BeautifulSoup
import requests
import csv
import re
import os
import urllib.request as req

url = 'https://movie.daum.net/ranking/boxoffice/weekly?date=20230821'
res = requests.get(url)
soup = BeautifulSoup(res.content, 'html.parser')
# print(soup.prettify())
ol = soup.select_one('.list_movieranking')
lis = ol.select('li')
arr = []
for i, li in enumerate(lis):
    if i > 1:
        # print(li)
        title = li.find('a', class_='link_txt').text
        day = li.find('span', class_='txt_num').text.replace(".","")
        count =  li.find_all('span', class_='info_txt')[1].text.replace("관객수","").replace(",","")
        url = li.find('a').get('href')
        img = li.find('img').get('src')
        print(title,day,count,url,img)
        arr.append([title,day,count,url,img])
with open('230828_230903.csv', 'w', encoding='utf-8') as f:
    write = csv.writer(f, delimiter='|', quotechar='"')
    for d in arr:
        write.writerow(d)