from unicodedata import name
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

name_list = [
  "성래, HLB",
  "유학, 한화에어로스페이스",
  "이지, 한화시스템",
  "준석, 하이닉스",
  "조정, 루트로닉",
  "민규, 메리츠화재",
  "빵태, 델타항공",
  "문수, 테라다인",
  "민중, LVMH",
  "우게, 뱅크오브아메리카",
  "지희, 애플",
  "씹솔, 알리바바",
  "원석, 테슬라",
  "용우, SNDL",
  "S&P500",
  "KOSPI",
]

cnt = 0

print(stock_list[0][1])

for i in range(len(stock_list)):
  # print(name_list[cnt])
  tmp_stock_price_list = [] # 현재 cnt에 해당하는 주식의 일자별 가격이 담길 임시 리스트
  # saved_path = "../backdata/" + str(cnt) + ".txt" # 현재 cnt에 해당하는 주식의 일자별 가격을 저장할 파일의 위치

  df = fdr.DataReader(stock_list[cnt][1],'2022-03-31')['Close']
  # print(len(df))  # df 안의 데이터 갯수, 2022-03-31부터 오늘까지의 날짜의 갯수와 같음
  
  # tmp_stock_price_list에 현재 cnt에 해당하는 주식의 일자별 가격을 담음
  for i in range(len(df)):
    tmp_stock_price_list.append(round((df[i] - df[0]) / df[0] * 100, 2))  # 수익률을 소수 셋째 자리에서 반올림 함

  # print(tmp_stock_price_list)
  # print(str(tmp_stock_price_list))

  edited_lines = [] # 수정된 파일 내용이 임시로 저장될 리스트
  current_price_earning_ratio_list_string = "\t\t\t\tname: \"" + str(name_list[cnt]) + "\", data: " + str(tmp_stock_price_list) + ",\n"   # 현재 cnt에서 수정할 데이터

  with open("./custom-highlight.js") as f:
    lines = f.readlines()
    for line in lines:
      # 조건에 따라 원하는 대로 line을 수정
      if name_list[cnt] in line:
        edited_lines.append(current_price_earning_ratio_list_string)
      else:
        edited_lines.append(line)

  with open("./custom-highlight.js", 'w') as f:
      f.writelines(edited_lines)

  cnt += 1



# 출력 결과 저장을 위한 파일 open
# sys.stdout = open('stockprice.txt', 'w')

# 전체 목록 출력
# df_list = [fdr.DataReader(code, '2022-03-31')['Close'] for name, code in stock_list]
# print(len(df_list)) # 종목 갯수 출력
# print(len(df_list['HLB'])) # 첫날부터 오늘까지의 날짜의 갯수 출력
# print(df_list)

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
# sys.stdout.close()
