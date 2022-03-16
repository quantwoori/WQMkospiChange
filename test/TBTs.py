from backtest.BTs import IndexChangeM
from backtest.BTs import Proactive, Reactive


# TEST: IndexChangeM
ic = IndexChangeM()
a, b = ic.change(2021, '1q')

c, d = ic.change(2021, '2q')
w0 = ic.change_date(2021, '1q')
w1 = ic.change_date(2021, '2q')

# TEST: Proactive
p = Proactive()
dfp = p.match_price(year=2021, quarter='2q')
dfp_rtn = p.calc_return(dfp)

# TEST: Reactive
r = Reactive()
dfr = r.match_price(year=2021, quarter='2q')
dfr_rtn = r.calc_return(dfr)

print(dfp_rtn)