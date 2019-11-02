a = input()
b = input()

a = set(a)
b = set(b)


flag = False

for i in a:
    for j in b:
        if i == j:
            flag = True
print("YES" if a & b else "NO")