class Node:
    def __init__(self,value,indexs):
        self.value = value
        self.indexs = indexs
        self.children = set()
    def addChild(parent,node):
        parent[0].children.add(node[0]) #passing by reference
    def removeChild(parent,node):
        parent[0].children.remove(node[0])
    def setChildren(parent,childrenArr):
        parent[0].children = childrenArr
    def __getChildren__(node):
        arr=[]
        for child in node[0].children:
            arr.append([child])
        return arr
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
    def __getChildrenArr__(self): #for node n1 with children c1 c2, return [[n1,c1],[n1,c2]]
        arr=[]
        for child in self.children:
            arr.append([child])
        for innerArr in arr:
            innerArr.append(self)
        return arr
    def getSRi(node, i): #return array of arrays of all sri's of size i+1 (consequent+ antedecent)
        if (i == 0):
            return Node.__getChildrenArr__(node[0])
        arr=[]
        for child in node[0].children:
            granChildren = Node.getSRi([child],i-1)
            if (len(granChildren) > 0):
                if (not node[0].value == "ROOT"):
                    for innerArr in granChildren:
                        innerArr.append(node[0])
                        arr.append(innerArr)
                else :
                    for innerArr in granChildren:
                        arr.append(innerArr)
        return arr

    def __getChildrenArr2__(self):
        arr=[]
        for child in self.children:
            arr.append([child.value])
        for innerArr in arr:
            innerArr.append(self.value)
        return arr
    def getSRi2(node, i): #same as SRi but with values so it's readable
        if (i == 0):
            return Node.__getChildrenArr2__(node[0])
        arr=[]
        for child in node[0].children:
            granChildren = Node.getSRi2([child],i-1)
            if (len(granChildren) > 0):
                if (not node[0].value == "ROOT"):
                    for innerArr in granChildren:
                        innerArr.append(node[0].value)
                        arr.append(innerArr)
                else :
                    for innerArr in granChildren:
                        arr.append(innerArr)
        return arr
   
