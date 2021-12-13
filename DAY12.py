from collections import defaultdict
import time

def pursueEnd_part1(map, current, smallsVisited, nPaths, currentPath):
    paths = currentPath + [current]
    if current == "start":
        paths = currentPath
    smalls = set(smallsVisited)
    for n in map[current]:
        if n == "start":
            continue
        elif n == "end":
            if paths[0] in map["start"]:
                nPaths.add(tuple(paths + ["end"]))
            continue
        if n.islower():
            if n in smallsVisited:
                continue
            smalls.add(n)
        pursueEnd_part1(map, n, smalls, nPaths, paths)
        if n.islower():
            smalls.remove(n)

def pursueEnd_part2(map, current, smallsVisited, nPaths, currentPath):
    paths = currentPath + [current]
    smalls = dict(smallsVisited)
    for n in map[current]:
        if n == "start":
            continue
        elif n == "end":
            if paths[1] in map["start"]:
                nPaths.add(tuple(paths + ["end"]))
            continue
        if n.islower():
            if n in smalls.keys():
                if smalls[n]==0:
                    smalls[n] += 1
                elif 2 in smalls.values():
                    continue
                else:
                    smalls[n] += 1
            else:
                smalls[n] = 1
        pursueEnd_part2(map, n, smalls, nPaths, paths)
        if n.islower():
            if smalls[n] > 0:
                smalls[n] -= 1


with open("DAY12.txt", "r") as file:
    caveMap = defaultdict(lambda : [])
    testSet = set()
    t0 = time.time()
    for line in file:
        caves = line.strip().split("-")
        caveMap[caves[0]].append(caves[1])
        caveMap[caves[1]].append(caves[0])
    nPaths = set()
    #paths = pursueEnd_part1(caveMap, "start", set(), nPaths, [])
    paths = pursueEnd_part2(caveMap, "start", {}, nPaths, [])
    print(time.time()-t0)
    print(len(nPaths))
            
        