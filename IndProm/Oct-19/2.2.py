with open("input.txt", 'r') as f:
    data = f.readlines()
d = data[0].split("\n")[0].split(" ")
a = []
print(d)
for i in d:
    if i != '':
        a.append(int(i))
print(a)
with open("output.txt", 'w') as f:
    if len(a):
        for i in range(0, len(a)):
            if i + 1 == a[i]:
                f.write(str(a[i]) + ' ')
    else:
        f.write("No solution")