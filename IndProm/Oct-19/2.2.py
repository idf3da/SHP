with open("input.txt", 'r') as f:
    data = f.read().split()

count = list()

for i in range(len(data)):
    if i == int(data[i]) - 1:
        count.append(data[i])

with open("output.txt", 'w') as f:
    if len(count) == 0:
        f.write('No solution')
    else:
        for i in count:
            f.write(i + ' ')