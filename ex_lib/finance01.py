# pip install matplotlib
# pip install finance-datareader
import FinanceDataReader as fdr
import matplotlib
import matplotlib.font_manager as fm
from matplotlib import pyplot as plt
import pandas as pd
from ex_db.DBManager import DBManger
import requests
import json

font_path = "gulim.ttc"
font_nm = fm.FontProperties(fname=font_path).get_name()
plt.rcParams['font.family'] = font_nm
plt.rcParams['axes.unicode_minus'] = False
# 국내/해외 지수, 환율정보, 국채금리정보
# apple = fdr.DataReader('TSLA')
# print(apple.head())
# apple['Close'].plot()
# plt.show()
# 한국 거래소 상장종목
# df_krx = fdr.StockListing('KRX')
# print(df_krx.head())
# KOSPI = df_krx[df_krx['Market'].str.contains('KOSPI')]
# print(KOSPI.columns)
# print(KOSPI.head(50))
# df_samsung_2022 = fdr.DataReader('005930', '2022')
# df_samsung_2000_2022 = fdr.DataReader('005930', '2000-01-01','2020-12-31')
# print(df_samsung_2000_2022.info())      #기본정보
# print(df_samsung_2000_2022.describe())  #기초통계량
#
# df_samsung_2000_2022['Close'].plot()
# plt.show()
import datetime
# 오늘 날짜를 기준으로 1달 전의 날짜 계산
end_date = datetime.date.today()
start_date = end_date - datetime.timedelta(days=30)
print(start_date)

mydb = DBManger()
sql = """SELECT * FROM stocks WHERE rownum <=5"""
df = pd.read_sql(con=mydb.conn, sql=sql)
print(df.head())

# 5개 종목 리스트(삼성, sk하이닉스, 셀트리온, 삼성바이오로직스. LG화학)
# stocks = ['005930', '000660', '068270', '207940', '051910']
# nm = ['삼성전자', 'sk하이닉스', '셀트리온', '삼성바이오로직스', 'LG화학']
# plt.figure(figsize=(12, 6))
# # 각 종목별로 주가 데이터 가져와서 그래프 그리기
# for i, stock in enumerate(stocks):
#     df = fdr.DataReader(stock, start_date, end_date)
#     plt.plot(df['Close'], label=nm[i])
#     file_nm = '{0}_{1}_{2}.xlsx'.format(nm[i], start_date, end_date)
#     writer = pd.ExcelWriter(file_nm, engine='openpyxl')
#     df.to_excel(writer, 'sheet1')
#     writer._save()
#
# plt.title('stock price')    # 제목
# plt.xlabel('Date')          # x축라벨
# plt.ylabel('Price')         # y축라벨
# plt.legend()                # 범례표시
# plt.grid(True)              # 그리드 표시 false안그려짐
# plt.tight_layout()          # 레이아웃 조정
# plt.savefig("30일.png")     # 파일로 저장
# plt.show()                  # 출력

