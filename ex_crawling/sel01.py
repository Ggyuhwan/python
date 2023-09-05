from selenium import  webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup

# 옵션 초기화
# 드라이버 초기화
driver = webdriver.Edge('./msedgedriver.exe')
driver.implicitly_wait(3)   # 브라우저 켜질때까지 기다리기
url = 'https://www.msn.com/ko-kr/news/techandscience'
driver.get(url)
time.sleep(3)
cnt = 5
pagedown = 1
body = driver.find_element(By.TAG_NAME, 'body')

while pagedown < cnt:
    body.send_keys(Keys.PAGE_DOWN)  # 스크롤 내리기
    time.sleep(1)
    print(body)
    pagedown += 1
# soup = BeautifulSoup(driver.page_source, 'html.pagepaeser')   # 멜론 406 안뜨게 하기
# print(soup.prettify())