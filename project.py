import numpy as np
import pandas as pd
import copy
# reading nursery.data csv file from github url
#url = 'https://raw.githubusercontent.com/ohadhell/Data_Stream_Privacy/main/nursery.data'
url2 = 'https://raw.githubusercontent.com/ohadhell/Data_Stream_Privacy/main/etsy.csv'
dataBase =  pd.read_csv('etsy.csv', sep=",",header=0)
data_size = len(dataBase.index) #number of transactions in data file
window_size = 5     #each sliding window size - chosen by us 
window_step = 2     #each step between two windows - chosen by us
window=[]           #the main window
left_trans = list(range(data_size)) #keeping track of the remaining transactions

# print(data.iloc[1]['Parents']) #way to print specific row specific column
# print(data.iloc[[1,2,3]]) 
#np.random.choice(range(20), 10, replace=False) 

#initializing the first sliding window
def sliding_window_init():
  rand_trans = np.random.choice(range(data_size), window_size, replace=False)
  for n in rand_trans:
    window.append(int(n))
    left_trans.remove(int(n))
  return window
window1= sliding_window_init()


#sliding the current window to the next one according to window_step
def slide_window(current_window):
  Wdel = np.random.choice(current_window, window_step, replace=False)
  Wadd = np.random.choice(left_trans, window_step, replace=False)
  for n in Wdel:
    current_window.remove(int(n))
  for n in Wadd:
    current_window.append(int(n))
    left_trans.remove(int(n))
  return current_window

print(dataBase.iloc[window1]) 
slide_window(window1)
print(dataBase.iloc[window1]) 
slide_window(window1)
print(dataBase.iloc[window1]) 