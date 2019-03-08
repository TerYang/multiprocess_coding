import numpy as np
import time
import pandas as pd
# a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# t0 = time.time()
# a += 1                 # 0.011219
# t1 = time.time()
# print('%f'%(t1-t0))
# t2 = time.time()
# print(np.add(a, 1, out=a) )   # 0.008843
# t3 = time.time()
# print('%f'%(t3-t2))

# 随机生成1000个数据
data = pd.Series(np.random.randn(1000), index=np.arange(1000))
print(data)
# 为了方便观看效果, 我们累加这个数据
print(data.cumsum())
