from proc.P0 import KCP0
from proc.P1 import KCP1
from proc.P2 import KCP2
from proc.P3 import KCP3

# Test1 >> Process1
p0 = KCP0('q2')
a, b, c, d = p0.main(20220221)

# Test2 >> Process2
p1 = KCP1(a, b, c, d)
e, f = p1.main()  # 후보군 시가총액, 후보 거래대금

# Test3 >> Process3
p2 = KCP2(e, f)
g = p2.get_sector_sep()

# Test4 >> Process4
p3 = KCP3(e, f, g)
h = p3.selection()
