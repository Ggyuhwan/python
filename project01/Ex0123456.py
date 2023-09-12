import pandas as pd
import xlsxwriter
import html5lib
url = 'https://www.korswim.co.kr/page/14?cate=006001'
tables = pd.read_html(url)
# print(len(tables), "개의 테이블이 있습니다")
tables[1]
df = pd.DataFrame(tables[0]) #남자
df1 = pd.DataFrame(tables[1]) #여자

writer = pd.ExcelWriter('swim.xlsx', engine='openpyxl')
# 2. 생성 파일에 시트명 지정 후 dataframe에 저장한 결과값 넣기
df.to_excel(writer, sheet_name='sheet1')
df1.to_excel(writer, sheet_name='sheet2')

# 3. 작성 완료 후 파일 저장
writer.close()

df[1]