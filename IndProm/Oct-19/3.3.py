with open("maze.in", "r", encoding="UTF-8") as f:
        lines = f.readlines()
        n, m = map(int, lines[0].split())
        symbols_map = {0: ' ', 1: '#', 2: 'x', 3: '_', 4: '!', 5: '*'}
        i = 0
        file = open("maze.out", "w")
        for ii in range(len(lines)):
            if i != 0:
                line = lines[ii]
                numbers = map(int, line.split())
                for number in numbers:
                    file.write(symbols_map[number])
                file.write("\n")
            i += 1
        file.close()