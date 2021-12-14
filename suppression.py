from window import Window

def intersection(lst1, lst2): #intersecting two arrays
    lst3 = [value for value in lst1 if value in lst2]
    return lst3

def items_transactions_cover(window: Window): #returning dictioanry of {"item" : [transactions it appears in]}
    transactions_cover= {}
    for item in Window.items_in_window(window):
        i = 0
        arr=[]
        for trans in Window.getTransactions(window):
            if (trans.__contains__(item)):
                arr.append(i)
            i+=1
        transactions_cover[item] = arr
    return transactions_cover

def inter_string(item1,item2): #returning the concatination of two strings ordered alphabetically
    if (item1 > item2):
        return (str(item2)+str(item1))
    return (str(item1)+str(item2))

#creating the next cover intersection, key is combiantion of the the two previous 
#keys ordered alphabetically, val is intersection of arrays of the apeared-in transactions
def next_cover_intersection(transCover):
    new_trans_cover={}
    for item1 in transCover:
        for item2 in transCover:
            if (not item1==item2):
                newArr = intersection(transCover[item1],transCover[item2])
                if (len(newArr) > 0):
                    new_trans_cover[inter_string(item1,item2)]=newArr
    return new_trans_cover