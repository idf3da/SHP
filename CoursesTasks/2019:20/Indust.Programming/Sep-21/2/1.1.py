c = 0
avg = 0
s = 0
a = []
b = []
i = -1

while i != 0:
    i = int(input())
    a.append(i)
    s += i
    c += 1
    
avg = s / c
c = 0

a.pop() #Remove zero

for i in a:
    if i > avg:
        b.append(i)
        c += 1
print(c)
print(*b)
