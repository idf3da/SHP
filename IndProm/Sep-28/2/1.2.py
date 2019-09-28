lines_c = 0
symb_c = 0
lines = []

with open("in.txt", "r", encoding="utf-8") as f:
    line = f.readline()
    lines.append(line)
    while line:
        line = f.readline()
        lines.append(line)
    lines = lines[::2]
    for i in lines:
        i = i[:-2]
    print(lines)