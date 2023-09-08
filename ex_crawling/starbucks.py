import xlsxwriter
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
from bs4 import BeautifulSoup
import time
import chromedriver_autoinstaller
import img_util
from PIL import Image
search_map=""
chromedriver_autoinstaller.install()
url = 'https://www.starbucks.co.kr/store/store_map.do'

def fn_search_map():
    print('스타 벅스')
    driver = webdriver.Chrome()

    driver.get(url)
    time.sleep(1)
    driver.find_element(By.XPATH,'//*[@id="container"]/div/form/fieldset/div/section/header[1]/h2/a').click()
    time.sleep(2)
    driver.find_element(By.XPATH,'//*[@id="container"]/div/form/fieldset/div/section/article[1]/article/header[2]/h3/a').click()
    time.sleep(2)
    driver.find_element(By.XPATH,'//*[@id="container"]/div/form/fieldset/div/section/article[1]/article/article[2]/div[1]/div[2]/ul/li[5]/a').click()
    time.sleep(2)
    driver.find_element(By.XPATH,'//*[@id="mCSB_2_container"]/ul/li[1]/a').click()
    time.sleep(2)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    lis=soup.select('.quickSearchResultBoxSidoGugun  li')
    arr = []
    for li in lis:
        title = li.select_one('strong').text
        lat = li.get('data-lat')
        long = li.get('data-long')
        address = li.select_one('.result_details').text
        address1 = address[:-9]
        num = address[-9:]

        arr.append([title,lat,long,address1,num])
    workbook = xlsxwriter.Workbook("star.xlsx")
    worksheet = workbook.add_worksheet()
    # 엑셀에 작성
    for row_num, row_data in enumerate(arr):
        for col_num, col_data in enumerate(row_data):
            worksheet.write(row_num, col_num, col_data)
    workbook.close()
    # print(arr)
fn_search_map()