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

### 논리 2 증명

