class BinarySearchTreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self,data):
        if data == self.data:
            return 

        if data < self.data:

            if self.left:
                self.left.add_child(data)
            else: 
                self.left = BinarySearchTreeNode(data)

        else:
        
            if self.right:
                self.right.add_child(data)
            else: 
                self.right = BinarySearchTreeNode(data)
    
    def in_order_traversal(self):
        elements =[]

        if self.left:
            elements += self.left.in_order_traversal()

        elements.append(self.data)

        if self.right:
            elements += self.left.in_order_traversal()
    
def build_tree(elements):
    root = BinarySearchTreeNode(elements[0])

    for i in range(1, len(elements)):
        root.add_child(elements[i])
    print("My Name:",elements)
    return root

if __name__ == '__main__':
    Name = ("J","O","S","E","P","H","S","I","M","O","N","S","P","R","U","D","E","N","T","E")
    name_tree = build_tree(Name)
    
  




