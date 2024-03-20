import queue

class treeNode:
    def __init__(self, data):
        self.data = data
        self.leftChild = None 
        self.rightChild = None  # Sửa thành rightChild

newBT = treeNode("Drinks")
leftChild = treeNode("Hot")
rightChild = treeNode("Cold")  # Sửa thành rightChild
newBT.leftChild = leftChild
newBT.rightChild = rightChild  # Sửa thành rightChild

def pre0rderTraversal(root):
    if root:
        print(root.data)  # Sửa thành root.data
        pre0rderTraversal(root.leftChild)  # Sửa thành leftChild
        pre0rderTraversal(root.rightChild)  # Sửa thành rightChild

def inorderTraversal(rootNode):
    if not rootNode:
        return
    inorderTraversal(rootNode.leftChild)  # Sửa thành leftChild
    print(rootNode.data)
    inorderTraversal(rootNode.rightChild)  # Sửa thành rightChild

def postorderTraversal(rootNode):
    if not rootNode:
        return
    postorderTraversal(rootNode.leftChild)  # Sửa thành leftChild
    postorderTraversal(rootNode.rightChild)  # Sửa thành rightChild
    print(rootNode.data)

def levelorderTraversal(rootNode):
    if not rootNode:
        return
    else:
        CustomQueue = queue.Queue()
        CustomQueue.put(rootNode)
        while not CustomQueue.empty():
            root = CustomQueue.get()
            print(root.data)  # In giá trị của nút mà không cần truy cập thuộc tính data
            if root.leftChild is not None:
                CustomQueue.put(root.leftChild)
                
            if root.rightChild is not None:
                CustomQueue.put(root.rightChild)

levelorderTraversal(newBT)
