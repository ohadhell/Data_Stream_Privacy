import numpy as np
import pandas as pd
from efficient_apriori import apriori

col_Not_Used=["ID","Dt_Customer","Z_CostContact","Z_Revenue","Response","Complain","AcceptedCmp3","AcceptedCmp4","AcceptedCmp5","AcceptedCmp1",
"AcceptedCmp2"]
col_list = ["Year_Birth","Education","Marital_Status","Income","Kidhome","Teenhome",
"Recency","MntWines",	"MntFruits",	"MntMeatProducts",	"MntFishProducts",
"MntSweetProducts",	"MntGoldProds",	"NumDealsPurchases",	"NumWebPurchases",	"NumCatalogPurchases",
"NumStorePurchases"	,"NumWebVisitsMonth"]

dataBase =  pd.read_csv('marketing_campaign.csv', sep="\t",header=0,usecols=col_list)
data_size = len(dataBase.index) #number of transactions in data file
window_size = 500     #each sliding window size - chosen by us 
window_step = 200     #each step between two windows - chosen by us
window=[]           #the main window
left_trans = list(range(data_size)) #keeping track of the remaining transactions


for col in col_list: #adding the column name to each item
     dataBase[col] = dataBase[col].replace(dataBase[col].unique(),list(map((lambda a: str(col)+": "+str(a)),dataBase[col].unique()))) 

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



transactions = [tuple(row) for row in dataBase.iloc[window1].values.tolist()]
itemsets, rules = apriori(transactions, min_support=0.3, min_confidence=0,output_transaction_ids=True)
print(rules)
print("NEW WINDOW")
slide_window(window1)
transactions = [tuple(row) for row in dataBase.iloc[window1].values.tolist()]
itemsets, rules = apriori(transactions, min_support=0.3, min_confidence=0,output_transaction_ids=True)
print(rules)
#transactions = [('eggs', 'bacon', 'soup'),('eggs', 'bacon', 'apple'),('soup', 'bacon', 'banana')]




#print(dataBase.iloc[window1]) 
#slide_window(window1)
#print(dataBase.iloc[window1]) 
#slide_window(window1)
#print(dataBase.iloc[window1]) 