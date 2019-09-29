class Date():
    def __init__(self, d, m, y):
        self.day = d
        self.month = m
        self.year = y
    def print(self):
        print("day:", self.day)
        print("month:", self.month)
        print("year:", self.year)

a = list(map(int, input().split(".")))
b = list(map(int, input().split(".")))
c = list(map(int, input().split(".")))

a = Date(a[0], a[1], a[2])
b = Date(b[0], b[1], b[2])
c = Date(c[0], c[1], c[2])

if (b.year >= c.year >= a.year) and (b.month >= c.month >= a.month) and (b.day >= c.day >= a.day):
    print("YES")
else:
    print("NO")