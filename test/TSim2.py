from proc.S1 import GeneratePrice
from datetime import datetime


stk = ['005930', '000660', '000020']
start_ = datetime(2021, 11, 1)
end_ = datetime(2022, 3, 14)
tgt_ = datetime(2022, 4, 30)
gp = GeneratePrice(
    stocks=stk,
    start_date=start_,
    end_date=end_,
    target_date=tgt_
)
a, b, c = gp.stat_price()
d = gp.stks_num()
e = gp.days_to_date(end_, tgt_, 0)
f = gp.gen_path(stk[0], c, a, b, e)
g = gp.gen_brownian()
