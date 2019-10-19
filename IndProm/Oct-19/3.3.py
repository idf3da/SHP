n=input().split()
n[0]=int(n[0])
n[1]=int(n[1])
a=[]
for i in range(n[0]):
    l=input().split()
    l = [int(l[j]) for j in range(n[1])]
    a.append(l)
for i in range(n[0]):
    for j in range(n[1]):
        if (a[i][j]==0):
            print(" ", end="")
        elif (a[i][j]==1):
            print("#", end="")
        elif (a[i][j] == 2):
            print("x", end="")
        elif (a[i][j] == 3):
            print("_", end="")
        elif (a[i][j] == 4):
            print("!", end="")
        else:
            print("*", end="")
    print()
