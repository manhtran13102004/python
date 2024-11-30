class Employee:
    def __init__(self, id, name):
        self.id = id
        self.name = name
    def delete(self):
        del self.id
        del self.name
e1 = Employee("1", "manh")
del e1.id
try:
    print(e1.id)
except AttributeError:
    print("Khong the in")

del e1
try:
    del e1
except NameError:
    print("Khong the xoa")
