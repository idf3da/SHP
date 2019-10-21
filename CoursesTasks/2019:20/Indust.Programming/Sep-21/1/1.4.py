n = int(input())
a = list(map(int, input().split()))

max_i = 0
min_i = 0

max_el = a[max_i]
min_el = a[min_i]

for i in range(0, n):
    if a[i] < min_el:
        min_el = a[i]
        min_i = i
    if a[i] > max_el:
        max_el = a[i]
        max_i = i
    
a[min_i] = max_el
a[max_i] = min_el

print(*a)