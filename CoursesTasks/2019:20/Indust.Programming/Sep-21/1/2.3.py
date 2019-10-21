def sign(a):
    if a < 0:
        return -1
    elif a == 0:
        return 0
    elif a > 0:
        return 1

a, b = list(map(int, input().split()))

print(sign(a) + sign(b))