import time
import threading
from collections import deque

class Queue:
    
    def __init__(self):
        self.queue = deque()
    
    def push(self, value):
        self.queue.appendleft(value)
        
    def pop(self):
        if len(self.queue) == 0:
            print('Can not pop')
        else:
            return self.queue.pop()
    
    def empty(self):
        return len(self.queue) == 0
    
orders = ['pizza','samosa','pasta','biryani','burger']
queue = Queue()

def placing():
    for order in orders:
        queue.push(order)
        time.sleep(0.5)
        print(f'Placing {order} successfully')
    
def serving():
    while queue.empty() == False:
        time.sleep(1.5)
        print(f'Serving {queue.pop()} successfully')

def print_bin(start, end):
    if end < start:
        return
    n = end
    start = bin(start)[2:]
    end = bin(end)[2:]
    bin_queue = Queue()
    bin_queue.push(start)
    for _ in range(n):
        candidate = bin_queue.pop()
        print(candidate)
        if candidate == end:
            return
        bin_queue.push(candidate + '0')
        bin_queue.push(candidate + '1')
        
if __name__ == '__main__':
    # thread1 = threading.Thread(target=placing)
    # thread2 = threading.Thread(target=serving)
    # thread1.start()
    # thread2.start()
    print_bin(1, 10)