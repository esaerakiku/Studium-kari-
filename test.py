import pandas as pd
import numpy as np

import pickle

datas = pd.DataFrame({}) # empty dataframe

raw = input('配列を入力してください') # A:{'A' : '15' , 'B' : '20' , 'C' : '40'}
searchword = raw.split(':',1)[0] # A
searchresults = raw.split(':',1)[1] # {'A' : '15', 'B' : '20', 'C' : '40'}
results = searchresults.replace(':', ',') # {'A' : '15', 'B' : '20', 'C' : '40'} -> {'A' , '15', 'B' , '20', 'C' , '40'}
results = results.replace('{', '')  # {'A' , '15', 'B' , '20', 'C' , '40'} -> 'A' , '15', 'B' , '20', 'C' , '40'
results = results.replace('}', '') # 'A' , '15', 'B' , '20', 'C' , '40' -> 'A' , '15', 'B' , '20', 'C' , '40'
results = results.replace("'", '') # 'A' , '15', 'B' , '20', 'C' , '40' -> A , 15, B , 20, C , 40
results = results.replace(' ', '') # A , 15, B , 20, C , 40 -> A,15,B,20,C,40
results = results.split(',') # A,15,B,20,C,40 -> ['A','15','B','20','C','40']

values = results[1::2] # ['15', '20', '40']
indexes = results[::2] # ['A', 'B', 'C']
data = pd.Series(values, index=indexes, name=searchword) # A: A 15 B 20 C 40
# print(searchresults)
# print(values)
# print(indexes)
datas = datas.append(data) # append the series to the dataframe
# print(datas) # confirm the dataframe

datas.to_pickle('./dataout_out.zip')
# d3 = pd.DataFrame({'Initial':['B','F','W'], 'Name':['boo', 'foo', 'woo']}, columns=['Name','Initial'])
# print(d3)
