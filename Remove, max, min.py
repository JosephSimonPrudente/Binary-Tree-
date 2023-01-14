class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data:
            return # node already exist

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


    def search(self, val):
        if self.data == val:
            return True

        if val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False

        if val > self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False

    def in_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.in_order_traversal()

        elements.append(self.data)

        if self.right:
            elements += self.right.in_order_traversal()

        return elements


    def delete(self, val):
        if val < self.data:
            if self.left:
                self.left = self.left.delete(val)
        elif val > self.data:
            if self.right:
                self.right = self.right.delete(val)
        else:
            if self.left is None and self.right is None:
                return None
            elif self.left is None:
                return self.right
            elif self.right is None:
                return self.left

            min_val = self.right.min()
            self.data = min_val
            self.right = self.right.delete(min_val)

        return self

    def max(self):
        if self.right is None:
            return self.data
        return self.right.max()

    def min(self):
        if self.left is None:
            return self.data
        return self.left.min()



def build_tree(elements):
    print("full Name:",elements)
    root = BinarySearchTreeNode(elements[0])

    for i in range(1,len(elements)):
        root.add_child(elements[i])

    return root
if __name__ == '__main__':
    Name = ("J","O","S","E","P","H","S","I","M","O","N","S","P","R","U","D","E","N","T","E")
    name_tree = build_tree(Name)
    print("In order Traversal:",name_tree.in_order_traversal())
  
    name_tree.delete("D")
    print("After deleting D: ",name_tree.in_order_traversal())

    print("Min", name_tree.min())
    print("Max:", name_tree.max())