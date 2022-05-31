import FinanceDataReader as fdr
import pandas as pd

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

df_list = [fdr.DataReader(code, '2022-03-31')['Close'] for name, code in stock_list]
len(df_list)
# print(df_list[0])
# print(type(df_list))
# print(df_list)

# pd.concat()로 합치기

df = pd.concat(df_list, axis=1)
df.columns = [name for name, code in stock_list] 
df.head(10)

print(df[['HLB']])

# import sys

# sys.stdout = open('stockprice.txt', 'w')

# print(df)

# sys.stdout.close()



# df = fdr.DataReader('028300','2022-03-31')
# df2 = fdr.DataReader('SNDL','2022-03-31')

# print(type(df.Open))
# print(df.Close)
# print(df2.Close)
# print(df2)