with open("input.txt", 'r') as f:
    data = f.readlines()
d = data[0].split("\n")[0].split(" ")
print(d)
with open("output.txt", 'w') as f:
    for i in range(0, len(d)):
        if i + 1 == int(d[i]):
            f.write(str(d[i]) + ' ')
