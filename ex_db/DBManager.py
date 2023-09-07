import cx_Oracle


class DBManger:
    def __init__(self):
        self.conn = None
        self.get_connection()
    def get_connection(self):
        self.conn = cx_Oracle.connect("java", "oracle", "localhost:1521/xe")
        return self.conn
    def __del__(self):
        try:
            print("소멸자")
            if self.conn:
                self.conn.close()
        except Exception as err:
            print("__del__", str(err))
    def insert(self, query, param):
        cursor = self.conn.cursor()
        cursor.execute(query, param)
        self.conn.commit()
        cursor.close()

if __name__ == '__main__':
    maneger = DBManger()
    conn = maneger.get_connection()
    sql = """INSERT INTO TB_USER (user_id, user_pw, user_nm)
                VALUES(:1, :2, :3)
            """
    maneger.insert(sql, ['test', 'test', 'test'])
    print(conn.version)