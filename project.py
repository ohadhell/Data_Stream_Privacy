from efficient_apriori import apriori
from window import Window
import suppression as sp
from node import Node2
import pandas as pd
from treelib import Node, Tree

##########constants########### 
dataSet='marketing_campaign.csv'
window_size = 2
window_step = 1
col_Not_Used=["ID","Dt_Customer","Z_CostContact","Z_Revenue","Response","Complain","AcceptedCmp3","AcceptedCmp4","AcceptedCmp5","AcceptedCmp1",
"Year_Birth","AcceptedCmp2"]
col_list = ["Education","Marital_Status","Income","Kidhome","Teenhome"]
#,"Recency","MntWines",	"MntFruits",	"MntMeatProducts",	"MntFishProducts",
#"MntSweetProducts",	"MntGoldProds",	"NumDealsPurchases",	"NumWebPurchases",	"NumCatalogPurchases",
#"NumStorePurchases"	,"NumWebVisitsMonth"]
##########constants########### 

#creating a window
theWindow = Window(dataSet,window_size,window_step,col_list)
print("ILOC:")
print(theWindow.curr_window)
print("TREE:")
tree=Tree()
n=Node2("a",[0,2])
tree.create_node(n)
tree.show()


still_sliding = True #boolean to indicate the sliding is finished -> meaning we slid all the dataSet


#while(still_sliding):
      #items_list= Window.items_in_window(theWindow) #saving all possible values
      #algorithm....
      #still_sliding = Window.slide_window(theWindow)




#transactions = Window.getTransactions(theWindow)
#itemsets, rules = apriori(transactions, min_support=0.3, min_confidence=0.2,output_transaction_ids=True)







