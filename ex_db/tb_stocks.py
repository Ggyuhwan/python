import sqlite3
from apscheduler.schedulers.blocking import BlockingScheduler
import sqlite03
import requests
import json
import datetime
conn = sqlite3.connect('mydb.db')
cur = conn.cursor()
cur.execute("SELECT * FROM stocks")
rows = cur.fetchall()
# print(rows)
cur = conn.cursor()
url = "https://api.upbit.com/v1/ticker?markets="
sql = """INSERT INTO tb_stocks VALUES(:1,:2,:3)"""
def test_interval():
    for row in rows:
        # print(url + row[0])
        res = requests.get(url + row[0])
        if res.status_code == 200:
            json_data = json.loads(res.text)
            market = json_data[0]['market']
            trade_price = "{:.15f}".format(json_data[0]['trade_price'])
            trade_timestamp = json_data[0]['timestamp'] * 0.001  # 초단위로 변환
            str_timestamp = \
                datetime.datetime.fromtimestamp(trade_timestamp).strftime(
                    "%Y-%m-%d %H:%M:%S")
            # print(market,trade_price,str_timestamp)
            cur.execute(sql, [market,trade_price,str_timestamp])
conn.commit()
conn.close()
sched = BlockingScheduler()
sched.add_job(test_interval, 'interval', seconds=500)
sched.start()