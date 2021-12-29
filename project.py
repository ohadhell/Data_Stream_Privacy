from numpy import NaN, dtype
from efficient_apriori import apriori
from window import Window
import suppression as sp
from node import Node
import pandas as pd

##########constants########### 
dataSet='marketing_campaign.csv'
window_size = 500
window_step = 200
col_Not_Used=["ID","Dt_Customer","Z_CostContact","Z_Revenue","Complain"
,"AcceptedCmp4","AcceptedCmp5","AcceptedCmp1","AcceptedCmp2","AcceptedCmp3","Recency","MntWines"]

col_list = ["Kidhome","Income","Year_Birth"
,"Education","Marital_Status","Response","Teenhome"]#,	"MntFruits","MntMeatProducts",	"MntFishProducts"]
#,"MntSweetProducts",	"MntGoldProds",	"NumDealsPurchases",	"NumWebPurchases",	"NumCatalogPurchases",
#"NumStorePurchases"	,"NumWebVisitsMonth"]
##########constants########### 

#creating a window
theWindow = Window(dataSet,window_size,window_step,col_list)
theSecondWindow = Window(dataSet,window_size,window_step,col_list)
still_sliding = True #boolean to indicate the sliding is finished -> meaning we slid all the dataSet
while(still_sliding):
      print("BEFORE: ")
      transactions = Window.getTransactions(theWindow)
      itemsets, rules = apriori(transactions, min_support=0.2, min_confidence=0.2,output_transaction_ids=True)
      print(rules)
      root = sp.createTree(theWindow)
      root2 = sp.createTree(theSecondWindow)
      loss1 = sp.suppress([root],[theWindow])
      loss2 = sp.suppressMin([root2],[theSecondWindow])
      print("loss 1: ",loss1,"  loss 2 : ",loss2)
      print("AFTER SUPPRESSION: ")
      transactions = Window.getTransactions(theWindow)
      itemsets, rules = apriori(transactions, min_support=0.2, min_confidence=0.2,output_transaction_ids=True)
      print(rules)
      still_sliding = Window.slide_window(theWindow)
      Window.slide_window(theSecondWindow)



















