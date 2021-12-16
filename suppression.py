from window import Window
from node import Node2


def intersection(lst1, lst2): #intersecting two arrays
    lst3 = [value for value in lst1 if value in lst2]
    return lst3

def createTree(window: Window): #returning root array of initial items in the current window
    #create first layer
    firstLayer= []
    for item in Window.items_in_window(window):
        i = 0
        arr=[]
        for trans in Window.getTransactions(window):
            if (trans.__contains__(item)):
                arr.append(i)
            i+=1
        firstLayer.append(Node2(item,arr)) #adding a new node to the root 
        #finished first layer
    for node in firstLayer:
        create_next_layers([node],firstLayer)
        
    return Node2("ROOT",firstLayer)

def create_next_layers(parent, parent_bros):
    parent=parent[0] #passing by reference
    children=[]
    for i in range(len(parent_bros)):
        if (not parent is parent_bros[i]):
            intersec = intersection(Node2.__getIndexs__(parent),Node2.__getIndexs__(parent_bros[i]))
            if(len(intersec) > 0):
                child = Node2(Node2.__getValue__(parent_bros[i]),intersec)
                Node2.addChild([parent],[child])
                children.append(child)
    for node in children:
        create_next_layers([node],children)

