# pip install cx_Oracle
import cx_Oracle
conn = cx_Oracle.connect("java", "oracle", "localhost:1521/xe")
print(conn.version)
sql ="""
    SELECT *
    FROM member
    WHERE mem_name LIKE '%' || :word || '%'
    ORDER BY mem_name ASC
"""
nm = input("검색하고 싶은 고객명 입력:")
d = {"word":nm}
with conn:
    cur = conn.cursor()
    rows = cur.execute(sql, d)
    for row in rows:
        print(row)