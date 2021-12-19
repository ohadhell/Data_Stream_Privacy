class Node:
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
        return Node.__printHelp(node,0)
    def __printHelp(node,layer): #private helper method to print tree
        res = str(node[0].value) +"\n"
        for child in node[0].children:
            for i in range(layer):
              res+="\t"  
            res+="|"
            res+=str(Node.__printHelp([child],layer+1))
        return res
    #def getLayer(root,layer):
        #if(layer == 0)