import FinanceDataReader as fdr
import pandas as pd
import sys  # 출력해서 저장하기 위한 용도

stock_list = [
  ["HLB", "028300"],
  ["한화에어로스페이스", "012450"],
  ["한화시스템", "272210"],
  ["하이닉스", "000660"],
  ["루트로닉", "085370"],
  ["메리츠화재", "000060"],
  ["델타항공", "DAL"],
  ["테라다인", "TER"],
  ["LVMH", "LVMH"],
  ["뱅크오브아메리카", "BAC"],
  ["애플", "AAPL"],
  ["알리바바", "BABA"],
  ["테슬라", "TSLA"],
  ["SNDL", "SNDL"],
  ["S&P500", "US500"],
  ["KOSPI", "KS11"],
]

# 출력 결과 저장을 위한 파일 open
sys.stdout = open('stockprice.txt', 'w')

# 전체 목록 출력
df_list = [fdr.DataReader(code, '2022-03-31')['Close'] for name, code in stock_list]
print(len(df_list)) # 종목 갯수 출력
print(len(df_list['HLB'])) # 첫날부터 오늘까지의 날짜의 갯수 출력
print(df_list)

# # pd.concat()로 합치기

# df = pd.concat(df_list, axis=1)
# df.columns = [name for name, code in stock_list] 
# df.head(10)

# 개별 출력
# df = fdr.DataReader('028300','2022-03-31')['Close']
# df2 = fdr.DataReader('SNDL','2022-03-31')
# print(type(df.Open))
# print(df['2022-03-31']) # 2022/03/31의 주식 가격
# print(df[0])            # 첫날의 주식 가격
# # print(df[0][0])       # Error
# print(len(df))          # 첫날부터 오늘까지의 날짜의 갯수 출력
# print(type(df))               # <class 'pandas.core.series.Series'>
# print(type(df['2022-03-31'])) # <class 'numpy.int64'>
# print(df2.Close)
# print(df2)

# 출력 결과 저장을 위한 파일 close
sys.stdout.close()
