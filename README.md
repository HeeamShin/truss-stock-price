# TRS Stock

Who is the king of investment?

## Function Specification

### Shown Data Example

| Name | Item | Start Price | Current Price | Delta (%) | Rank |
|------|------|-------------|---------------|-----------|------|
| A | HLB | import | import | calc | calc |

### Back Data Example

| Name | Item | DAY_START | DAY_TODAY | DAY_END |
|------|------|-----------|-----------|---------|
| A | HLB | 28738 | 23782 | 32738 |

### How to

- [x] `finance-data-reader.py`에서 날짜별 종목 가격 추출
- [ ] 추출된 데이터에서 한 명분 column 분리
- [ ] 분리된 column 당 날짜별 수익률 계산
- [ ] 계산된 수익률 리스트로 변환
- [ ] 변환된 리스트를 `custom-highlight.js`에 넣기
- [ ] 모든 사람에 대해 2 ~ 5 반복
