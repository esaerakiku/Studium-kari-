import pandas as pd
import numpy as np

# リストからシリーズの作成
s1 = pd.Series([0,1,2])
print(s1)

# 配列からシリーズの作成
s2 = pd.Series(np.random.rand(3))
print(s2)

# 辞書からシリーズの作成
s3 = pd.Series({0:'boo',1:'foo',2:'woo'})
print(s3)

# 多次元リストからデータフレームの作成
d1 = pd.DataFrame([[0,1,2],[3,4,5],[6,7,8],[9,10,11]], index=[10,11,12,13], columns=['c1','c2','c3'])
print(d1)

# 多次元配列からデータフレームの作成
d2 = pd.DataFrame(np.random.rand(12).reshape(4,3), columns=['c1','c2','c3'])
print(d2)

# 辞書からデータフレームの作成
d3 = pd.DataFrame({'Initial':['B','F','W'], 'Name':['boo', 'foo', 'woo']}, columns=['Name','Initial'])
print(d3)