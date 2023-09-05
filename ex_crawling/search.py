from selenium import  webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup
# https://pcmap.place.naver.com/place/list?query=%EB%8C%80%EC%A0%84%EC%88%98%EC%98%81%EC%9E%A5&x=127.38495079999785&y=36.35043960000061&clientX=126.9504&clientY=36.552825&bounds=127.24727837567974%3B36.13224152202446%3B127.52948967939051%3B36.56251287064558&ts=1693910670889&mapUrl=https%3A%2F%2Fmap.naver.com%2Fp%2Fsearch%2F%EB%8C%80%EC%A0%84%EC%88%98%EC%98%81%EC%9E%A5
driver = webdriver.Edge('./msedgedriver.exe')
driver.implicitly_wait(3)   # 브라우저 켜질때까지 기다리기
url = 'https://pcmap.place.naver.com/place/list?query=%EB%8C%80%EC%A0%84%EC%88%98%EC%98%81%EC%9E%A5&x=127.38495079999785&y=36.35043960000061&clientX=126.9504&clientY=36.552825&bounds=127.24727837567974%3B36.13224152202446%3B127.52948967939051%3B36.56251287064558&ts=1693910670889&mapUrl=https%3A%2F%2Fmap.naver.com%2Fp%2Fsearch%2F%EB%8C%80%EC%A0%84%EC%88%98%EC%98%81%EC%9E%A5'
driver.get(url)
time.sleep(3)
soup = BeautifulSoup(driver.page_source,'html.parser')
content = soup.select('span')
lis = soup.find_all('span', class_='place_bluelink YwYLL')
print(lis)
# print(content.prettify())
# lis = content.find_all('li')
# for li in lis:
#     print(lis)


# print(soup.prettify())

