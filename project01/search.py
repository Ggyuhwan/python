import json
import requests
from bs4 import BeautifulSoup
# url = 'https://www.korswim.co.kr/page/14?cate=006001'
# res = requests.get(url)
# soup = BeautifulSoup(res.content, 'html.parser')
# l_tag = soup.find('div', class_='s14-2-bot')
# trs = l_tag.find_all('tr')
data = []
for i in range(1,8):
    url = 'https://www.korswim.co.kr/page/14?cate=00600{0}'.format(str(i))
    res = requests.get(url)
    soup = BeautifulSoup(res.content, 'html.parser')
    l_tag = soup.find('div', class_='s14-2-bot')
    trs = l_tag.find_all('tr')
    part = soup.find('li', class_='s14-tab2-atv').text
    # dis = l_tag.find('td', class_='s14-td s14-td1').text
    print(part)


    for j, tr in enumerate(trs):
        if j == 0:
            print('th', tr.text)
        else:
            dis = l_tag.find('td').find_all(class_='s14-td s14-td1')
            # print('거리', tr.text)
            print(dis)
