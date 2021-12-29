import pandas as pd
import numpy as np

class Window:
    #initializing the first sliding window
    def __init__(self,dataSet,windowSize,windowStep,col_list):
        self.dataBase =  pd.read_csv(dataSet, sep="\t", header=0, usecols=col_list)
        data_size = len(self.dataBase.index) #number of transactions in data file
        self.window_size = windowSize     #each sliding window size 
        self.window_step = windowStep     #each step between two windows
        self.curr_window_index=[]           #the actual window - array of indexes from dataSet
        self.left_trans = list(range(data_size)) #keeping track of the remaining transactions
        rand_trans = np.random.choice(range(data_size), windowSize, replace=False)
        for n in rand_trans:
            self.curr_window_index.append(int(n))
            self.left_trans.remove(int(n))
        for col in col_list: #adding the column name to each item
            self.dataBase[col] = self.dataBase[col].replace(self.dataBase[col].unique(),list(map((lambda a: str(col)+": "+str(a)),self.dataBase[col].unique()))) 
        self.curr_window = self.dataBase.iloc[self.curr_window_index] #the actual window transactions
        

    #sliding the current window to the next one according to window_step
    def slide_window(self):
        if(self.window_step > len(self.left_trans)):
            return False
        Wdel = np.random.choice(self.curr_window_index, self.window_step, replace=False)
        Wadd = np.random.choice(self.left_trans, self.window_step, replace=False)
        for n in Wdel:
            self.curr_window_index.remove(n)
        for n in Wadd:
            self.curr_window_index.append(int(n))
            self.left_trans.remove(int(n))
        self.curr_window = self.dataBase.iloc[self.curr_window_index]
        return (True,Wdel,Wadd)

#return the transactions of the current window
    def getTransactions(self):
        return [tuple(row) for row in self.curr_window.values.tolist()]

    def items_in_window(self): # return array of all possible values at the current window
        items=[]
        for col in self.curr_window:
            for item in self.curr_window[col].unique():
                items.append(item)
        return items
    def suppressItem(self, item):
        (column,value) = item.split(": ")
        self.dataBase[column] = self.dataBase[column].replace([item], [np.NaN])
        self.curr_window = self.dataBase.iloc[self.curr_window_index]
        self.dataBase[column] = self.dataBase[column].replace([np.NaN], [item])
