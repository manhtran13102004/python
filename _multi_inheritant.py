class Teacher:
    
    def __init__(self):
        self.is_teacher = True
        
    def teach(self):
        print("teach")
    
    
class Student:
    
    def __init__(self):
        self.is_student = True
        
    def study(self):
        print("Study")
        
class Youtuber:
    
    def __init__(self):
        self.is_ytb = True
        
    def make_video(self):
        print("Make videos")
        
class Person(Teacher, Student, Youtuber):
    def __init__(self):
        Teacher.__init__(self)
        Student.__init__(self)
        Youtuber.__init__(self)

p1 = Person()
p1.teach()
p1.study()
p1.make_video()
print(p1.is_teacher)
print(p1.is_student)
print(p1.is_ytb)