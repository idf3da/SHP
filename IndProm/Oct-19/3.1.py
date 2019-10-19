n,m=map(int, input().split())
a=[]
for i in range(n):
    l=input().split()
    l=[int(l[j]) for j in range(m)]
    a.append(l)
for i in range(n):
    for j in range(m):
        if(a[i][j]==0):
            print(8, end=" ")
        else:
            print(a[i][j], end=" ")
    print()