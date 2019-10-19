bank = {}
k = int(input())
for i in range(k):
    com = list(input().split())
    if com[0] == "1":
        if com[1] in bank:
            bank[com[1]] += int(com[2])
        else:
            bank[com[1]] = int(com[2])
    else:
        if com[1] in bank:
            print(bank[com[1]])
        else:
            print("ERROR")
