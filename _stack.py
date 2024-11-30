from collections import deque

class Stack:
    
    def __init__(self):
        self.stack = deque()
        
    def push(self, value):
        self.stack.append(value)
        
    def pop(self):
        if len(self.stack) == 0:
            raise Exception
        return self.stack.pop()
    
    def peek(self):
        if len(self.stack) == 0:
            raise Exception
        return self.stack[-1]
    
    def is_empty(self):
        return len(self.stack) == 0
    
    def __bool__(self):
        return len(self.stack) > 0
    
def reverse_string(ori_string):
    stk = Stack()
    for c in ori_string:
        stk.push(c)
    new_string = ''
    while stk:
        new_string += stk.pop()
    return new_string 

def is_balanced(ori_string):
    stk = Stack()
    for c in ori_string:
        # print(c, end='')
        # print()
        if c not in ('(', '[', '{', ')', '}', ']'):
            continue
        elif c in ('(', '[', '{'):
            stk.push(c)
        else:
            if stk.is_empty():
                return False
            elif c == ')' and stk.peek() != '(':
                return False
            elif c == '}' and stk.peek() != '{':
                return False
            elif c == ']' and stk.peek() != '[':
                return False
            else:
                stk.pop()
        # print(stk.stack)
    return True

print(is_balanced("({a+b})"))   # --> True
print(is_balanced("))((a+b}{"))  # --> False
print(is_balanced("((a+b))"))    # --> Truprint(e
print(is_balanced("))"))         # --> False
print(is_balanced("[a+b]*(x+2y)*{gg+kk}")) # --> True