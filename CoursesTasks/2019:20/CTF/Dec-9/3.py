a = input()

flag = False

for i in range(0, len(a) - 1):
    if a[i] == a[i + 1] and a[i] == "3":
        flag = True
print("YES" if flag else "NO")