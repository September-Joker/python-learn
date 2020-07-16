import pandas as pd
import numpy as np

x = pd.Series([1, 2, np.nan, 3, 4, 5, 6, np.nan, 8])

# 检验序列中是否存在缺失值
a = x.hasnans     # 布尔值
print(a)

# 讲缺失值填充为平均值
# 原来的数据不变，需要重新赋值给新的变量
x1 = x.fillna(value=x.mean())

print(x1)

df3 = pd.DataFrame(
    {'A': [5, 3, None, 4],
     'B': [None, 2, 4, 3],
     'C': [4, 3, 8, 5],
     'D': [5, 4, 2, None]}
)
# 查看缺失值汇总
print(df3.isnull().sum())

# 用上一行填充
df4 = df3.ffill()
print(df3)
print(df4)

# 用上一列填充
df4 = df3.ffill(axis=1)
print(df3)
print(df4)

# 缺失值删除
print(df3.info())
df5 = df3.dropna()
print(df3)
print(df5)
