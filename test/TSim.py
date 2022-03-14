from proc.S0 import BrownianMotion

import pandas as pd
import matplotlib.pyplot as plt

# Test Brownian Motion
bm = BrownianMotion(70000)
test1 = pd.DataFrame(bm.gen_scaled_brownian(-0.02, std=0.8, step=1000))
test2 = pd.DataFrame(bm.gen_scaled_brownian(-0.02, std=0.8, step=1000))
test3 = pd.DataFrame(bm.gen_scaled_brownian(-0.02, std=0.8, step=1000))

test = pd.concat([test1, test2, test3], axis=1)
test.plot()
plt.show()
