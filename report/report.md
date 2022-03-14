# KOSPI, KOSPI200 Strategy

## Hypothesis
<p>
2달 전부터 예측해서 주식을 산다면? 초과 이익이 있을 것이다. 
</p>

<p>
논리 전개

1. 2달 전 예측했을때 초과 이익이 있다.
2. 2달 전 예측을 잘 하면 된다. 
</p>


### 논리 1 증명
```
import backtest.BTs import Proactive
import backtest.BTs import Reactive

# TEST: Proactive
p = Proactive()
dfp = p.match_price(year=2021, quarter='1q')
dfp_rtn = p.calc_return(dfp)

# TEST: Reactive
r = Reactive()
dfr = r.match_price(year=2021, quarter='1q')
dfr_rtn = r.calc_return(dfr)

# Compare result of dfp_rtn and dfr_rtn
```
<p>
패키지 내의 Proactive, Reactive 클래스 사용.
결과물은 다음과 같음.
</p>

```
# Proactive (2 months ago)
{
    '005850': 0.16226411, 
    '009900': 0.03238094, 
    '138040': 0.035658956, 
    '178920': -0.009727597, 
    '329180': 0.033492804
}

# Reactive (1 months ago)
{
    '005850': -0.06097561, 
    '009900': -0.09060401, 
    '138040': 0.0014992952, 
    '178920': 0.082978725, 
    '329180': -0.08860761
}
```
<p> 
본 결과는 2021년 2분기 인덱스 변경임.
Proactive는 변경 2달 전에 매매를 시작하였고, 
Reactive는 변경 1달 전에 매매를 시작함. 
확실한 성과 차이를 볼 수 있음. 5종목 중 4종목이 Proactive 시 아웃퍼폼함.
</p>

### 논리 2 모델 및 증명


