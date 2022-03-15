from proc.P0 import KCP0
from proc.P1 import KCP1
from proc.P2 import KCP2
from proc.P3 import KCP3

from datetime import datetime

# Test1 >> Process1
p0 = KCP0('q2', designate=datetime(2021, 10, 29))
a, b, c, d = p0.main(20211029)

# Test2 >> Process2
p1 = KCP1(a, b, c, d, parachute=['007700', '259960', '323410', '361610', '383800'])
"""
[
'007700', '383800' : 분할상장 이슈
'259960', '323410', '361610' : 특별 편입 
]
"""
e, f = p1.main()  # 후보군 시가총액, 후보 거래대금

# Test3 >> Process3
p2 = KCP2(e, f, designate=datetime(2021, 10, 29))
g = p2.get_sector_sep()

# Test4 >> Process4
p3 = KCP3(e, f, g)
h = p3.selection()
k = p3.amend_selection(selection=h)
