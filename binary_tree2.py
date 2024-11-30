class BinTreeNode:
    
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
    def add(self, value):
        if self.value == value:
            return
        elif value < self.value:
            if self.left:
                self.left.add(value)        
            else:
                self.left = BinTreeNode(value)
        elif value > self.value:
            if self.right:
                self.right.add(value)
            else:
                self.right = BinTreeNode(value)
    
    def in_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.in_order_traversal()
        elements.append(self.value)
        if self.right:
            elements += self.right.in_order_traversal()
        
        return elements
    
    def left_most_val(self):
        if not self.left:
            return self.value
        return self.left.left_most_val()
    
    def right_most_val(self):
        if not self.right:
            return self.value
        return self.right.right_most_val()
    
    def delete(self, value):
        if value < self.value:
            if self.left:
                self.left = self.left.delete(value)
        elif value > self.value:
            if self.right:
                self.right = self.right.delete(value)
        else:
            if not self.left and not self.right:
                return None
            elif not self.left:
                return self.right
            elif not self.right:
                return self.left
            else:
                # left_most_val = self.right.left_most_val()
                # self.value = left_most_val
                # self.right = self.right.delete(left_most_val)
                right_most_val = self.left.right_most_val()
                self.value = right_most_val
                self.left = self.left.delete(right_most_val)
                        
        return self
    
node = BinTreeNode(5)
node.add(7)
node.add(1)
node.add(4)
node.add(-2)
node.add(12)
node.add(3)
# node.delete(1)
# node.delete(5)
# node.delete(-2)
# node.delete(12)
# node.delete(3)
# node.delete(4)
node.delete(7)
# node.delete(5)
print(node.in_order_traversal())