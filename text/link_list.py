class Node:

    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class LinkedList:

    def __init__(self, num_list=[]):
        self.head = Node(0)
        for num in num_list:
            self.insert_values(num)

    def insert_values(self, vals=[]):
        cur = self.head
        while cur.next:
            cur = cur.next

        for val in vals:
            cur.next = Node(val)
            cur = cur.next

    def __str__(self):
        s = ""
        cur = self.head.next
        while cur:
            s += str(cur.val) + "-->"
            cur = cur.next
        return s

    def insert_after_value(self, data_after, data_to_insert):
        cur = self.head.next
        while cur and cur.val != data_after:
            cur = cur.next

        if cur == None:
            raise Exception("Value Not Found")

        insert_node = Node(data_to_insert, cur.next)
        cur.next = insert_node

    def remove_by_value(self, data):
        cur = self.head
        while cur and cur.next and cur.next.val != data:
            cur = cur.next

        if not cur or not cur.next:
            print("Value Not Found")
            return
        
        cur.next = cur.next.next

    def print(self):
        cur = self.head.next
        while cur:
            print(f'{cur.val}==>', end='')
            cur = cur.next
        print()
        
class DoubleNode:
    
    def __init__(self, val = None, pre = None, next = None):
        self.val = val
        self.pre = pre
        self.next = next
        
class DoubleLinkedList:
    
    def __init__(self, vals=[]):
        self.head = DoubleNode(0)
        cur = self.head
        for val in vals:
            cur.next = DoubleNode(val, cur, None)
            cur = cur.next
        self.tail = cur
    
    def print_forward(self):
        cur = self.head.next
        while cur:
            print(f'{cur.val}==>', end='')
            cur = cur.next
        
        print()
        
    def print_backward(self):
        cur = self.tail
        while cur != self.head:
            print(f'{cur.val}==>', end='')
            cur = cur.pre
        
        print()    
# ll = LinkedList()
# ll.insert_values(["banana", "mango", "grapes", "orange"])
# ll.print()
# ll.insert_after_value("mango", "apple")  # insert apple after mango
# ll.print()
# ll.remove_by_value("orange")  # remove orange from linked list
# ll.print()
# ll.remove_by_value("figs")
# ll.print()
# ll.remove_by_value("banana")
# ll.remove_by_value("mango")
# ll.remove_by_value("apple")
# ll.remove_by_value("grapes")
# ll.print()

dll = DoubleLinkedList([1, 2, 3, 4, 5])
dll.print_backward()