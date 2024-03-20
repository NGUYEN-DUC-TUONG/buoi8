class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def contains(self, value):
        temp = self.root
        while temp:
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else:
                return True
        return False

# Sử dụng lớp BinarySearchTree và Node
bst = BinarySearchTree()
bst.root = Node(10)
bst.root.left = Node(20)
bst.root.right = Node(40)
bst.root.left.left = Node(30)
bst.root.left.right = Node(50)

# Kiểm tra xem các giá trị cụ thể có tồn tại trong cây hay không
print(bst.contains(10))  
print(bst.contains(40)) 
print(bst.contains(50)) 