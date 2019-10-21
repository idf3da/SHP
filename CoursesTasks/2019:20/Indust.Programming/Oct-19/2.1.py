with open("in.txt", 'r') as f:
    data = f.readlines()
with open("out.txt", 'w') as f:
    f.write(str(len(data)) + '\n')
    string = "".join("".join(data).split('\n'))
    f.write(str(len(string)) + '\n')
    if len(data) > 2:
        f.write(data[2])
    else:
        f.write('0\n')
