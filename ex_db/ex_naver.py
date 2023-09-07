import requests
import  DBManager as mydb
import json

import mylogger
from apscheduler.schedulers.blocking import BlockingScheduler
db = mydb.DBManger()
log = mylogger.make_logger()
log.info("start")
insert_sql= """
INSERT INTO stocks( item_code, stock_nm, close_price,compare_close)
VALUES (:1,:2,:3,:4)
"""
# for i in range(1, 43):
def test_interval():
    for i in range(1, 2):
        url ="https://m.stock.naver.com/api/stocks/marketValue/KOSPI?page={0}&pageSize=50".format(str(i))
        print(url)
        res = requests.get(url)
        jsonObj = json.loads(res.text)
        stock_arr = jsonObj['stocks']
        # print(stock_arr[2])
        for row in stock_arr:
            # print(row['itemCode'], row['stockName'], row['closePrice'],row['compareToPreviousClosePrice'])
            db.insert(insert_sql,[row['itemCode'], row['stockName']
                    , row['closePrice'],row['compareToPreviousClosePrice']])
         # 종목코드, 종목명, 종가, 변동가 출력
# log.info("start !!! ")
sched = BlockingScheduler()
sched.add_job(test_interval, 'interval', seconds=600)
sched.start()