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
  tmp_stock_price_list = [] # 현재 cnt에 해당하는 주식의 일자별 가격이 담길 임시 리스트

  df = fdr.DataReader(stock_list[cnt][1],'2022-03-31')['Close']
  # print(len(df))  # df 안의 데이터 갯수, 2022-03-31부터 오늘까지의 날짜의 갯수와 같음
  
  # tmp_stock_price_list에 현재 cnt에 해당하는 주식의 일자별 가격을 담음
  for i in range(len(df)):
    date = "Date.UTC(" + str(df.index[i].year) + ", " + str(df.index[i].month - 1) + ", " + str(df.index[i].day) + ")" # 날짜 정보 저장
    price_earning_ratio = round((df[i] - df[0]) / df[0] * 100, 2) # 수익률을 소수 셋째 자리에서 반올림 함
    tmp_stock_price_list.append([date, price_earning_ratio])
  
  tmp_stock_price_list_with_date = "" # 날짜 정보와 수익률을 문자열로 저장
  
  for d, p in tmp_stock_price_list:
    delta = "[" + d + ", " + str(p) + "], "
    tmp_stock_price_list_with_date += delta

  edited_lines = [] # 수정된 파일 내용이 임시로 저장될 리스트
  current_price_earning_ratio_list_string = "\t\t\t\tname: \"" + str(name_list[cnt]) + "\", data: [" + tmp_stock_price_list_with_date + "],\n"   # 현재 cnt에서 수정할 데이터

  with open("./chart-drawer.js", 'rt', encoding='UTF8') as f:
    lines = f.readlines()
    for line in lines:
      # 조건에 따라 원하는 대로 line을 수정
      if name_list[cnt] in line:
        edited_lines.append(current_price_earning_ratio_list_string)
      else:
        edited_lines.append(line)

  with open("./chart-drawer.js", 'w', encoding='UTF8') as f:
      f.writelines(edited_lines)

  cnt += 1
