n=int(input())
a=input().split()
a=[int(i) for i in a]
for i in range(n):
    print(a[i]*a[n-1], end=' ')