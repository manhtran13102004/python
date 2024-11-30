class Fibonacci:
    def __init__(self, limit):
        self.limit = limit
        self.index = 0
        self.before1 = None
        self.before2 = None
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index == 0:
            self.before1 = 0
            self.index += 1
            return 0
        elif self.index == 1:
            self.before2 = self.before1
            self.before1 = 1
            self.index += 1
            return 1
        elif self.before1 + self.before2 > self.limit:
            raise StopIteration
        
        self.index += 1
        cur = self.before1 + self.before2
        self.before2 = self.before1
        self.before1 = cur
        return cur
    
f1 = Fibonacci(200)
for num in f1:
    print(num, end=' ')