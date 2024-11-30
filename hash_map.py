# with open('text/text.txt', 'r') as f:
#     f.readline()
#     temps = []
#     for line in f.readlines():
#         temps.append(int(line.split(',')[1][:2]))
        
#     print(f'Average temperature: {sum(temps[0:7]) / len(temps[0:7])}')
#     print(f'Max temperatur: {max(temps)}')

# with open('text/text.txt', 'r') as f:
#     f.readline()
#     day_temp = {}
#     for line in f.readlines():
#         element = line.split(',')
#         element[1] = element[1].replace('\n','')
#         day_temp[element[0]] = int(element[1])
    
#     print(day_temp['Jan 9'])
#     print(day_temp['Jan 4'])

# with open('text/poem.txt','r') as f:
#     word_count = {}
#     for line in f.readlines():
#         words = line.split()
#         for i in range(len(words)):
#             words[i] = words[i].replace(',','').replace('.','').replace(':','')
#             word_count[words[i]] = 1 if words[i] not in word_count else word_count[words[i]] + 1
    
#     print(word_count)

# handling collision by chaning
# class HashTable:
    
#     def __init__(self):
#         self.max_size = 10
#         self.arr = [[] for _ in range(10)]
    
#     def hash(self, value):
#         return value % self.max_size
     
#     def __setitem__(self, key, value):
#         code = self.hash(key)
#         for index, tuple in enumerate(self.arr[code]):
#             if tuple[0] == key:
#                 del self.arr[code][index]
#                 break
#         self.arr[code].append([key, value])
        
#     def __getitem__(self, key):
#         code = self.hash(key)
#         for tuple in self.arr[code]:
#             if tuple[0] == key:
#                 return tuple[1]
#         return None
    
#     def __delitem__(self, key):
#         code = self.hash(key)
#         for i, tuple in enumerate(self.arr[code]):
#             if tuple[0] == key:
#                 del self.arr[code][i]

# handling collision by probing
# class HashTable:
    
#     def __init__(self, max_size = 10):
#         self.max_size = max_size
#         self.arr = [None for _ in range(self.max_size)]
        
#     def hash(self, key):
#         return hash(key) % self.max_size
    
#     def __setitem__(self, key, value):
#         code = self.hash(key)
#         found = False
#         while code < self.max_size and not found:
#             if self.arr[code] == None or self.arr[code][0] == key:
#                 found = True
#                 break
#             if code == self.max_size - 1:
#                 code = 0
#             else:
#                 code = code + 1
#         self.arr[code] = (key, value)
        
#     def __getitem__(self, key):
#         code = self.hash(key)
#         found = False
#         index = code
#         while code < self.max_size and not found:
#             if not self.arr[code]:
#                 return None
#             else:
#                 if self.arr[code][0] == key:
#                     return self.arr[code][1]
#                 else:
#                     code += 1
#         code = 0
#         while code < index and not found:
#             if not self.arr[code]:
#                 return None
#             else:
#                 if self.arr[code][0] == key:
#                     return self.arr[code][1]
#                 else:
#                     code += 1
    
#     def __delitem__(self, key):
#         code = self.hash(key)
#         found = False
#         while code < self.max_size and not found:
#             if not self.arr[code]:
#                 raise Exception
#             elif self.arr[code][0] == key:
#                 found = True
#                 self.arr[code] = None
#             else:
#                 code += 1
        
#         code = 0
#         while code < self.max_size and not found:
#             if not self.arr[code]:
#                 raise Exception
#             elif self.arr[code][0] == key:
#                 self.arr[code] = None
#             else:
#                 code += 1

class HashTable:
    
    def __init__(self, max_size = 10):
        self.max_size = max_size
        self.arr = [None for _ in range(self.max_size)]
        
    def hash(self, key):
        return hash(key) % self.max_size
    
    def take_prob_range(self, index):
        return [*range(index, self.max_size)] + [*range(0, index)]

    def __setitem__(self, key, value):
        code = self.hash(key)
        prob_range = self.take_prob_range(code)
        for index in prob_range:
            if not self.arr[index]:
                self.arr[index] = (key, value)
                break
            elif self.arr[index][0] == key:
                self.arr[index] = (key, value)
                break
    
    def __getitem__(self, key):
        code = self.hash(key)
        prob_range = self.take_prob_range(code)
        for index in prob_range:
            if not self.arr[index]:
                raise KeyError
            elif self.arr[index][0] == key:
                return self.arr[index][1]
       
    def __delitem__(self, key):
        code = self.hash(key)
        prob_range = self.take_prob_range(code)
        for index in prob_range:
            if not self.arr[index]:
                raise KeyError
            elif self.arr[index][0] == key:
                self.arr[index] = None
                break
            
# ht = HashTable()
# ht[4] = 5
# print(ht.arr)
# ht[14] = 8
# ht[5] = 9
# ht[5] = 1
# print(ht.arr)
# print(ht[23])
# dict = {2 : 3}
# print(dict[232])
# del dict[22]
# print(dict)
# print(ht.arr)
# print(ht[4])