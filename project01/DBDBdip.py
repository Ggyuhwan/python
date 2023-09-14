import pandas as pd
import sqlite3

# conn = sqlite3.connect("swim.db")
# scv = """CREATE TABLE swim(
#             distance      VARCHAR2(100)
#             ,world_pr     VARCHAR2(100)
#             ,olympics_pr   VARCHAR2(100)
#             ,asia_pr     VARCHAR2(100)
#             ,kor_pr     VARCHAR2(100)
#             )
# """
# cur = conn.cursor()
# cur.execute(scv)
# row = cur.fetchall()
# print(row)
# conn.close()
for i in range(1,8):
    url = 'https://www.korswim.co.kr/page/14?cate=00600{0}'.format(str(i))
    tables = pd.read_html(url)
    # print(len(tables), "개의 테이블이 있습니다")
    df = pd.DataFrame(tables[0]) #남자
    df1 = pd.DataFrame(tables[1]) #여자

    con = sqlite3.connect("C:\dev\pythonProject\project01\swim.db")
    df.to_sql('swim_M', con, if_exists='append')
    df1.to_sql('swim_G', con, if_exists='append')




