


class BinarySearchTreeNode:
    
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
    def add(self, value):
        if self.value == value:
            return
        elif value < self.value:
            if self.left == None:
                self.left = BinarySearchTreeNode(value)
            else:
                self.left.add(value)
        else:
            if self.right == None:
                self.right = BinarySearchTreeNode(value)
            else:
                self.right.add(value)
    
    def pre_order_traversal(self):
        pre_order_list = []
        
        pre_order_list.append(self.value)
        if self.left:
            pre_order_list += self.left.pre_order_traversal()
        if self.right:
            pre_order_list += self.right.pre_order_traversal()
            
        return pre_order_list
    
    def in_order_traversal(self):
        in_order_list = []
        
        if self.left:
            in_order_list += self.left.in_order_traversal()
        in_order_list.append(self.value)
        if self.right:
            in_order_list += self.right.in_order_traversal()
            
        return in_order_list
    
    def post_order_traversal(self):
        post_order_list = []
        
        if self.left:
            post_order_list += self.left.post_order_traversal()
        if self.right:
            post_order_list += self.right.post_order_traversal()
        post_order_list.append(self.value)
            
        return post_order_list
    
    def find_min(self):
        left_most_node = self
        while left_most_node.left:
            left_most_node = left_most_node.left
        return left_most_node.value
    
    def find_max(self):
        right_most_node = self
        while right_most_node.right:
            right_most_node = right_most_node.right
        return right_most_node.value
    
    def calculate_sum(self):
        sum = 0
        if self.left:
            sum += self.left.calculate_sum()
        sum += self.value
        if self.right:
            sum += self.right.calculate_sum()
        
        return sum
    
    
        
        
bstn = BinarySearchTreeNode(10)
bstn.add(5)
bstn.add(9)
bstn.add(1)
bstn.add(13)
bstn.add(22)
bstn.add(8)
bstn.add(21)

l = bstn.in_order_traversal()
print(l)
print(bstn.find_min())
print(bstn.find_max())
print(bstn.calculate_sum())
