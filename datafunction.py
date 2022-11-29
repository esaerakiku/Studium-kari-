import pandas as pd
import numpy as np
import pickle

def initialize(data):
    data = pd.DataFrame({}) # empty dataframe
    return data

def datainput(data):
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
    data = data.append(data) # append the series to the dataframe
    # print(datas) # confirm the dataframe
    return data

def dict_append(d, data): # d is a dictionary. data is a dataframe. データにディクショナリを追加する
    raw_converted = pd.DataFrame(d)
    data = data.append(raw_converted)
    return data


def dataoutput(data):
    print(data) # confirm the dataframe
    return data

def datalabel(data):
    print(data.index) # データの中にどんな単語が入っているのかを確認する

def datafrom(data,word):
    print(data[word]) # どの単語からwordに矢印が伸びているかを確認する。

def datato(data,word):
    print(data[:,word]) # どの単語にwordが矢印を伸ばしているかを確認する。

def datasave(data):
    data.to_pickle('./dataout_out.zip') # save the dataframe to zip file
    
def dataload(data):
    data = pd.read_pickle('./dataout_out.zip') # load the dataframe from zip file
    return data

# 以下使用例
# 最初にインプットするときは、datas = initialize(datas)で初期化する。
def main():
    data = initialize(data)
    d = {'key1' : [15] , 'key2' : [20] , 'key3' : [40]} # ここのdの入力にfor文を回して入力を入れて、for文の中でappendをすればいけるはず？
    data = dict_append(d, data)
    data = dataoutput(data)
    datasave(data)
    
if __name__ == '__main__':
    main()
    