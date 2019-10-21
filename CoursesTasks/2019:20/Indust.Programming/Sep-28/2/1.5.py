n = int(input())

class Student():
    def __init__(self):
        a = input().split(" ")
        self.name = a[0]
        self.surname = a[1]
        self.math = int(a[2])
        self.phys = int(a[3])
        self.inf = int(a[4])

a = []
b = [0, 0, 0]

for i in range(n):
    a.append(Student())

for i in a:
    b[0] += i.math
    b[1] += i.phys
    b[2] += i.inf

for i in b:
    print("{:f}".format(i / n), sep=" ")
