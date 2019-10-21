class Student:
    def __init__(self):
        self.name = ''
        self.sur = ''
        self.age = 0
        self.cl = 1
        self.count = 0
        self.marks = []
    def read_student(self):
        (self.name,self.surname,self.age,self.cl,self.count) = input().split()
        self.marks = [int(i) for i in input().split()]
        return self
    def print_student(self):
        print(self.name,self.surname,self.age,self.cl,self.count)
        print(*self.marks)

    def avg_mark(self):
        print("{:f}".format(sum(self.marks) / int(self.count)))

    def will_grad():
        return self.cl + c >= 11
    
a = []

c = int(input())
for i in range(5):
    a.append(Student.read_student(Student()))
    if i<4:
        input()

for i in a:
    Student.will_grad(c)