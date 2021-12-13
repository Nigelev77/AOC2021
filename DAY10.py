

with open("DAY10.txt", "r") as file:
    octopi = [[int(i) for i in line.strip()] for line in file]
    flashedAlready = [[False for i in range(len(octopi[0]))]for j in range(len(octopi))]
    flashes = 0
    totalOctopi = len(octopi) * len(octopi[0])
    step = 0
    count = 0
    while count != totalOctopi:
        count = 0
        for y in range(len(octopi)):
            for x in range(len(octopi[0])):
                octopi[y][x] += 1
        noFlash = False
        while not noFlash:
            noFlash = True
            for y in range(len(octopi)):
                for x in range(len(octopi[0])):
                    if octopi[y][x] >9 and not flashedAlready[y][x]:
                        flashedAlready[y][x] = True
                        if x>0:
                            if y>0:
                                octopi[y-1][x-1] += 1
                            if y<len(octopi)-1:
                                octopi[y+1][x-1] += 1
                            octopi[y][x-1] += 1
                        if x<len(octopi) - 1:
                            if y>0:
                                octopi[y-1][x+1] += 1
                            if y< len(octopi)-1:
                                octopi[y+1][x+1] += 1
                            octopi[y][x+1] += 1
                        if y>0:
                            octopi[y-1][x] += 1
                        if y<len(octopi) - 1:
                            octopi[y+1][x] += 1
                        flashes += 1
                        noFlash = False
        for y in range(len(octopi)):
            for x in range(len(octopi[0])):
                if flashedAlready[y][x]:
                    octopi[y][x] = 0
                    count += 1
        step += 1
        flashedAlready = [[False for i in range(len(octopi[0]))]for j in range(len(octopi))]
    print(step)
