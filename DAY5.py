import time
with open("DAY5.txt", "r") as file:
    intersectionsDict = {}
    t0 = time.time()
    for line in file:
        ends = line.split(" -> ")
        start = tuple(int(i) for i in ends[0].split(","))
        end = tuple(int(i) for i in ends[1].split(","))
        if start[0] == end[0]:
            step = 1 if start[1]<=end[1] else -1
            for y in range(start[1], end[1]+step, step):
                intersectionsDict[(start[0], y)] = intersectionsDict.setdefault((start[0], y), 0) + 1
        elif start[1] == end[1]:
            step = 1 if start[0]<=end[0] else -1
            for x in range(start[0], end[0]+step, step):
                intersectionsDict[(x,start[1])] = intersectionsDict.setdefault((x, start[1]), 0) + 1
        else:
            stepX = 1 if start[0]<=end[0] else -1
            stepY = 1 if start[1]<=end[1] else -1
            curPt = start
            while curPt != end:
                intersectionsDict[curPt] = intersectionsDict.setdefault(curPt, 0) + 1
                curPt = (curPt[0]+stepX, curPt[1]+stepY)
            intersectionsDict[end] = intersectionsDict.setdefault(end, 0) + 1
    twos = 0
    t1 = time.time()
    for val in intersectionsDict.values():
        if val>=2:
            twos+=1
    print(t1-t0)
    print(twos)
        