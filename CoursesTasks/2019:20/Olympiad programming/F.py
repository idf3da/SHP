input()
n = list(map(int, input().split()))

s = []
c = 0
flag = False

for i in range(1, len(n)):
    if n[i] == n[i - 1]:
        if flag:
            s[c] += 1
        else:
            s.append(1)
            flag = True
    else:
        if flag:
            flag = False

print(max(s) + 1)