from typing import runtime_checkable
from window import Window
from node import Node
import copy
iSensitive=["Income","Recency","Year_Birth"]
supportDict={}
p=0.5

def intersection(lst1, lst2): #intersecting two arrays
    lst3 = [value for value in lst1 if value in lst2]
    return lst3

def createTree(window: Window): #returning root array of initial items in the current window
    #create first layer
    window=window[0]
    firstLayer= []
    sensitives=[]
    for item in Window.items_in_window(window): 
        i = 0
        arr=[]
        for trans in Window.getTransactions(window):
            if (trans.__contains__(item)):
                arr.append(i)
            i+=1
        newNode=[Node(item,arr)]
        supportDict[item]=arr
        if(iSensitive.__contains__(item.rpartition(':')[0])):
            sensitives.append(newNode[0]) #adding a new node to the root if he's sensitive
        firstLayer.append(newNode[0]) #adding the node to firstLayer arr 
        #finished first layer
    #creating the root of the tree
    root = Node("ROOT",[])
    for i in range(len(sensitives)):
        create_next_layers([sensitives[i]],firstLayer) #[(i+1):]  slicing the children array so there will be no duplicates
        Node.addChild([root],[sensitives[i]]) #adding this node as a child of root
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

def sup(item):
    return len(supportDict[item])

def conf(rule):
    supXA = len(Node.__getIndexs__(rule[0])) #the indexs size of the most inner node of sri
    supX = supportDict[Node.__getValue__(rule[0])]
    for s in range(1,len(rule) - 1):
        supX = intersection(supX, supportDict[Node.__getValue__(rule[s])])
    if(len(supX) == 0):
        return 0
    return supXA/len(supX)

def C_item_sri(item, sri):
    counter = 0
    for rule in sri:
        if (hasValue(rule,item)):
            counter+=1
    return counter

def payOff(item, sri):
    sri=sri[0]
    return (C_item_sri(item, sri)) / sup(item)

def violatesP(rule):
    return conf(rule) >= p

def supressInTree(node, layer, item):
    childrenArr=[]
    if(layer>=0):
        for child in Node.__getChildren__(node):
            if (Node.__getValue__(child[0]) != item):
                supressInTree(child, layer-1, item)
                childrenArr.append(child)
    else:
        childrenArr = Node.__getChildren__(node)
    childrenSet=set()
    for child in childrenArr:
        childrenSet.add(child[0])
    Node.setChildren(node, childrenSet)

def hasValue(lst, mem):
    for node in lst:
        if(Node.__getValue__(node)==mem):
            return True
    return False
def copySri(sri):
    sri=sri[0]
    copy=[]
    for rule in sri:
        copy.append(rule)
    return copy


def suppress(root,window):
    window = window[0]
    root=root[0] #pointer
    i = 1
    loss = 0
    while(True):
        sriT = Node.getSRi([root], i) #all rules of size i+1
        if (len(sriT) == 0):
                break
        sri = filter(violatesP, sriT) #return all rules that violates p-uncertinty
        sri = list(sri)
        while (len(sri) > 0):
            maxPayoff = 0
            supItem = sri[0][0]
            #finding the item in all the rules with max payoff
            for rule in sri:
                for item in rule:       
                    currPayoff = payOff(Node.__getValue__(item), [sri])
                    if currPayoff > maxPayoff:
                        maxPayoff = currPayoff
                        supItem = item
            toRemoveArr = []
            for rule in sri:
                if (hasValue(rule, Node.__getValue__(supItem))):
                    toRemoveArr.append([rule])
            for rule in toRemoveArr:
                sri.remove(rule[0])
            Window.suppressItem([window],Node.__getValue__(supItem))
            supressInTree([root], i, Node.__getValue__(supItem))
            loss = loss+sup(Node.__getValue__(supItem))
        i+=1
    return loss

def suppressMin(root,window):
    window = window[0]
    root=root[0] #pointer
    i = 1
    loss = 0
    while(True):
        sriT = Node.getSRi([root], i) #all rules of size i+1
        if (len(sriT) == 0):
                break
        sri = filter(violatesP, sriT) #return all rules that violates p-uncertinty
        sri = list(sri)
        while (len(sri) > 0):
            supItem = sri[0][0]
            minPayoff = payOff(Node.__getValue__(supItem), [sri])
            #finding the item in all the rules with max payoff
            for rule in sri:
                for item in rule:       
                    currPayoff = payOff(Node.__getValue__(item), [sri])
                    if currPayoff < minPayoff:
                        minPayoff = currPayoff
                        supItem = item
            toRemoveArr = []
            for rule in sri:
                if (hasValue(rule, Node.__getValue__(supItem))):
                    toRemoveArr.append([rule])
            for rule in toRemoveArr:
                sri.remove(rule[0])
            Window.suppressItem([window],Node.__getValue__(supItem))
            supressInTree([root], i, Node.__getValue__(supItem))
            loss = loss+sup(Node.__getValue__(supItem))
        i+=1
    return loss

def filterSuppres(rules):
      return filter(lambda rule: hasSupp(rule.lhs) and hasSupp(rule.rhs), rules)
def hasSupp(lst):
    for item in lst:
        if(item == "SUPPRESSED"):
            return False
    return True
            
                










