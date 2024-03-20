class treeNode:
    def __init__(self, data, children = []):
        self.data = data
        self.chilren = children 
        
    def __str__(self, level=0):
        ret = " " * level + str(self.data) + "\n"
        for child in self.chilren:
            ret += child.__str__(level + 1)
        return ret
    
    def addChild(self, TreeNode):
        self.chilren.append(TreeNode)
        
tree = treeNode('Drinks' , [])
cold = treeNode('Cold' , [])
hot = treeNode('Hot' , [])
tree.addChild(cold)
tree.addChild(hot)
tea = treeNode('Tea' , [])
coffee = treeNode('Coffee' ,[])
cala = treeNode('Cola' , [])
hot.addChild(coffee)
hot.addChild(tea)
print(tree)