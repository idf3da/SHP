class Rectangle:
    def __init__(self, w, h):
        self.w = w
        self.h = h
    def width(self):
        return self.w
    def height(self):
        return self.h
    def area(self):
        return self.w * self.h
    def perimeter(self):
        return (self.w + self.h) * 2

a, b = list(map(int, input().split()))

rec = Rectangle(a, b)

print(rec.area(), rec.perimeter())