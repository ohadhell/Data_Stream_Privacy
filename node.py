class Node2:
    def __init__(self,value,indexs):
        self.value = value
        self.indexs = indexs
        self.children = set()
    def addChild(parent,node):
        parent[0].children.add(node[0]) #passing by reference
    def __getIndexs__(self):
        return self.indexs
    def __getValue__(self):
        return self.value
    def printSubTree(node): #passing by reference
        print(node[0].value)
        for child in node[0].children:
            print("\t|"+Node2.printSubTree([child])) 
    