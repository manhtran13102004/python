import time
import threading
from collections import deque

class Queue:
    
    def __init__(self):
        self.queue = deque()
    
    def add(self, value):
        self.queue.appendleft(value)
        
    def pop(self):
        return self.queue.pop()
    
    def len(self):
        return len(self.queue)
    
    def empty(self):
        return len(self.queue) == 0

def placing(queue, order):
    time.sleep(0.5)
    queue.add(order)
    print(f'Done adding {order}')

def serving(queue):
    time.sleep(2)
    print(f'Done serving {queue.pop()}')
    
    
orders = ['pizza','samosa','pasta','biryani','burger']
queue = Queue()


def bin_print(start, end):
    start = bin(start)[2:]
    end = bin(end)[2:]
    bin_queue = Queue()
    bin_queue.add(start)
    while True:
        candidate = bin_queue.pop()
        print(candidate)
        if candidate == end:
            break
        bin_queue.add(candidate + '0')
        bin_queue.add(candidate + '1')
        
# bin_print(1, 10)