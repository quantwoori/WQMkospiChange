# Seek Alpha with KOSPI200 지수변경

## 발단
<p>
코스피 200 지수변경 시, 1달 전에 발표 후 매매하는 것 보단, 2달 전 먼저 매매하는 것이 수익률이 훨씬 좋음
</p>

## BTs.py 와 TBTs.py 참조
```
# Proactive 매매시
{
    '005850': 0.16226411, 
    '009900': 0.03238094, 
    '138040': 0.035658956, 
    '178920': -0.009727597, 
    '329180': 0.033492804
}

# Reactive 매매시
{
    '005850': -0.06097561, 
    '009900': -0.09060401, 
    '138040': 0.0014992952, 
    '178920': 0.082978725, 
    '329180': -0.08860761
}
```

### 


## 형태


### 기준일까지 주가 예측 작업
<p>
몬테카를로 이용. 100,000회의 시뮬레이션을 통해서 편입 예정 종목을 찾아냄.
주가가 Brownian Motion을 따를 것이란 가정 하에 주가의 path를 생성하고 그에 따른 시가 총액 계산.
거래 대금은 일정한 평균을 유지할거라 가정.
</p>

### 코스피의 계산 작업
<p> 
./proc 내의 작업 파이프라인을 이용.

1. P0: 현재 종목들의 시가총액, 거래대금, 관리종목, 유통주식 조회
2. P1: 코스피 200 에 포함되지 않을 종목들을 골라냄. (6개월 미만, 관리종목, 유동성 기준 미달) 
3. P2: 섹터 안에서 유동시총으로 순서를 정하는 지수이기 때문에,섹터 안에서 나누는 작업 실시.
4. P3: P0~P3 에서 진행된 정보를 종합하여 섹터별 조건 충족하는 것을 뽑고 -> 200종목 미달일 경우 추가 종목을 뽑는 작업 실시

</p>

## main.py
<p>
 Reactive 작업과 Proactive 작업 실시. Proactive 는 몬테 카를로 시뮬레이션 결과를 시가총액 데이터 뒤에 붙여서 계산.
</p>