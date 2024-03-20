class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None


bst = BinarySearchTree()


print(bst.root) 


bst.root = Node(10)
print(bst.root.value)  
print(bst.root.left)  
print(bst.root.right)  