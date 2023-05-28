import pandas as pd
import numpy as np
import pickle

datas_from_pkl_zip = pd.read_pickle('./dataout_out.zip')
print(datas_from_pkl_zip) # confirm the dataframe
datas = datas_from_pkl_zip

raw = input('C:{'B' : '5' , 'C' : '10' , 'D' : '20'}のような配列を入力してください') # C:{'B' : '5' , 'C' : '10' , 'D' : '20'}
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
print(values)
# print(indexes)
datas = datas.append(data) # append the series to the dataframe
print(datas) # confirm the dataframe