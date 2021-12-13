import time

with open("DAY13.txt", "r") as file:
    coords = set()
    instructions = []
    for line in file:
        line = line.strip()
        if len(line)<1:
            continue
        elif not line.startswith('f'):
            coord = line.split(",")
            coords.add((int(coord[0]), int(coord[1])))
        elif line.startswith('f'):
            eq = line.split(" ")[2]
            instruction = eq.split("=")
            instructions.append((instruction[0], int(instruction[1])))

    t0 = time.time()
    for instruction in instructions:
        if instruction[0] == 'y':
            newCoords = set()
            y = instruction[1]
            for c in coords:
                dist = c[1]-y
                if dist>0:
                    newCoords.add((c[0], y-dist))
                else:
                    newCoords.add(c)
            coords = newCoords
        elif instruction[0] == 'x':
            newCoords = set()
            x = instruction[1]
            for c in coords:
                dist = c[0] - x
                if dist>0:
                    newCoords.add((x-dist, c[1]))
                else:
                    newCoords.add(c)
            coords = newCoords
    maxX = list(coords)[0][0]
    maxY = list(coords)[0][1]
    for c in coords:
        maxX = max(maxX, c[0])
        maxY = max(maxY, c[1])
    grid = [[' ' for i in range(maxX+1)]for j in range(maxY+1)]
    for c in coords:
        grid[c[1]][c[0]] = '#'
    print(time.time()-t0)
    for row in grid:
        print("".join(row))
    