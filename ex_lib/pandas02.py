# pandas db 조회하는 법
import pandas as pd
from ex_db.DBManager import DBManger
import requests
import json

mydb = DBManger()

merge_sql = """
MERGE INTO tb_stock_bbs a
USING dual
ON (a.item_code = :1
    and a.discussionId = :2)
WHEN MATCHED THEN
    UPDATE SET a.readCount = :3
                ,a.goodCount = :4
                ,a.badCount = :5
                ,a.commentCount = :6
WHEN NOT MATCHED THEN
    INSERT (a.item_code, a.discussionId, a.bbs_title, a.bbs_contents
    ,a.creatr_date, a.readCount, a.goodCount, a.badCount, a.commentCount, a.update_date)
    VALUES (:7, :8, :9, :10, to_date(:11,'YYYY-MM-DD HH24:MI:SS'), :12, :13, :14, :15, SYSDATE)

"""
sql = """SELECT * FROM stocks"""
df = pd.read_sql(con= mydb.conn, sql=sql)
print(df.head())
# dataFreame 순회하기
for index, row in df.iterrows():
    print(row['ITEM_CODE'], row['STOCK_NM'])
    # index로 접근
    print(df.iloc[index])
    code = row['ITEM_CODE']     # 종목 별
    url = "https://m.stock.naver.com/api/discuss/localStock/{0}?rsno=0&size=100".format(code)
    print(url)
    res = requests.get(url)
    json_data = json.loads(res.text)
    for v in json_data:
        discussionId = v['discussionId']
        title = v['title']
        contents = v['contents'][:1300]
        date = v['date'][:19]
        readCount = v['readCount']
        goodCount = v['goodCount']
        badCount = v['badCount']
        commentCount = v['commentCount']
        try:
            mydb.insert(merge_sql,[code, discussionId, readCount, goodCount
                                   , badCount, commentCount, code, discussionId
                                   , title, contents, date, readCount, goodCount
                                   , badCount, commentCount])
        except Exception as e:
            print(str(e))
    # print(json_data)



