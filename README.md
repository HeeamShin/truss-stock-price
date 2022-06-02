# TRUSS Stock Gamble

The winner takes it all.

## To Do

- [ ] 등수 표시기
- [ ] Commit 시간
- [x] 파일 정리

## How to Implement

1. `finance-data-reader.py`에서 한 종목을 고르고 2022-03-31부터 오늘까지의 가격을 추출 (종가 기준)
2. 추출한 가격들을 list에 저장
3. 저장한 list를 `js` 파일의 가격 데이터에 덮어씀
4. 1 ~ 3을 모든 종목에 대해 반복
5. [GitHub Actions](https://docs.github.com/en/actions)로 1~4 과정을 자동화
6. 자동화된 결과를 [Netlify](https://www.netlify.com/)로 호스팅
