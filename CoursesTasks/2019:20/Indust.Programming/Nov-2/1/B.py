class Fraction:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def __eq__(self, other):
        return self.a / self.b == other.a / other.b

a, b = list(map(int, input().split("/")))
c, d = list(map(int, input().split("/")))

fr1 = Fraction(a, b)
fr2 = Fraction(c, d)

print("YES" if fr1 == fr2 else "NO")