class AdultException(Exception):
    def __str__(self):
        return "Chua du tuoi"

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def get_minor_age(self):
        try:
            self.raiseAdultException()
        except AdultException as e:
            print(e)
    def raiseAdultException(self):
        if self.age < 18:
            raise AdultException()
        print("La nguoi lon")

p1 = Person("tu", 17)
p1.get_minor_age()
        
