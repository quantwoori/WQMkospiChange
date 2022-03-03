from proc.P0 import KCP0
from proc.P1 import KCP1


# Test1 >> Process1
p0 = KCP0('q2')
a, b, c, d = p0.main(20220221)

# Test2 >> Process2
p1 = KCP1(a, b, c, d)
e, f = p1.main()