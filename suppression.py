from window import Window
from node import Node


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
        firstLayer.append(Node(item,arr)) #adding a new node to the root 
        #finished first layer
    #creating the root of the tree
    root = Node("ROOT",[])
    for node in firstLayer:
        create_next_layers([node],firstLayer)
        Node.addChild([root],[node]) #adding this node as a child of root
    return root

def create_next_layers(parent, parent_bros):
    parent=parent[0] #passing by reference
    children=[]
    for i in range(len(parent_bros)):
        if (not parent is parent_bros[i]):
            intersec = intersection(Node.__getIndexs__(parent),Node.__getIndexs__(parent_bros[i]))
            if(len(intersec) > 0):
                child = Node((Node.__getValue__(parent_bros[i])),intersec)
                Node.addChild([parent],[child])
                children.append(child)
    for i in range(len(children)):
        create_next_layers([children[i]],children[(i+1):]) #slicing the children array so there will be no duplicates

