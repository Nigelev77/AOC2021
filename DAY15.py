import math

class Node:
    x = 0
    y = 0

    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def __init__(self) -> None:
        self.x = 0
        self.y = 0


def part_1():
    with open("DAY15.txt", "r") as file:
        weights = [[int(i) for i in line.strip()]for line in file]
        width = len(weights[0])
        calculatedWeights = [[math.inf for x in range(width)]for y in range(width)]
        nodes = [[Node() for i in range(width)]for j in range(width)]
        for y in range(width):
            for x in range(width):
                nodes[y][x].x = x
                nodes[y][x].y = y
        unvisited = [nodes[0][0]]
        visited = []
        unvisited[0].last = (-1, -1)
        calculatedWeights[0][0] = 0
        current = Node()
        while len(unvisited) != 0:
            unvisited.sort(key=lambda x : calculatedWeights[x.y][x.x])
            currentNode = unvisited.pop(0)
            xy = (currentNode.x, currentNode.y)
            currentWeight = calculatedWeights[xy[1]][xy[0]]
            if xy == (width-1, width-1):
                print(currentNode.last)
                break
            if xy[0] > 0:
                left = (xy[0]-1, xy[1])
                if calculatedWeights[left[1]][left[0]]>currentWeight+weights[left[1]][left[0]]:
                    calculatedWeights[xy[1]][xy[0]-1] = currentWeight + weights[left[1]][left[0]]
                    nodes[xy[1]][xy[0]-1].last = xy
                    unvisited.append(nodes[xy[1]][xy[0]-1])
            if xy[1] > 0:
                up = (xy[0], xy[1]-1)
                if calculatedWeights[up[1]][up[0]]>currentWeight+weights[up[1]][up[0]]:
                    calculatedWeights[up[1]][up[0]] = currentWeight + weights[up[1]][up[0]]
                    nodes[up[1]][up[0]].last = xy
                    unvisited.append(nodes[up[1]][up[0]])
            if xy[0] < width-1:
                right = (xy[0]+1, xy[1])
                if calculatedWeights[right[1]][right[0]]>currentWeight+weights[right[1]][right[0]]:
                    calculatedWeights[right[1]][right[0]] = currentWeight + weights[right[1]][right[0]]
                    nodes[right[1]][right[0]].last = xy
                    unvisited.append(nodes[right[1]][right[0]])
            if xy[1] < width-1:
                down = (xy[0], xy[1]+1)
                if calculatedWeights[down[1]][down[0]]>currentWeight+weights[down[1]][down[0]]:
                    calculatedWeights[down[1]][down[0]] = currentWeight + weights[down[1]][down[0]]
                    nodes[down[1]][down[0]].last = xy
                    unvisited.append(nodes[down[1]][down[0]])
        path = [['.' for i in range(width)]for j in range(width)]

        while currentNode.last != (-1, -1):
            path[currentNode.y][currentNode.x] = '#'
            currentNode = nodes[currentNode.last[1]][currentNode.last[0]]

        for row in path:
            print("".join(row))
        print(calculatedWeights[width-1][width-1])
    


with open("DAY15.txt", "r") as file:
    tile = [[int(i) for i in line.strip()]for line in file]
    tileWidth = len(tile)
    weights = [[0 for i in range(tileWidth*5)]for j in range(tileWidth*5)]
    for y in range(tileWidth*5):
        for x in range(tileWidth*5):
            tileX = x//tileWidth
            tileY = y//tileWidth
            added = tileX+tileY
            newWeight = tile[y%tileWidth][x%tileWidth] + added
            if newWeight > 9:
                newWeight -= 9
            weights[y][x] = newWeight
    width = len(weights)
    calculatedWeights = [[math.inf for x in range(width*5)]for y in range(width*5)]
    nodes = [[Node() for i in range(width)]for j in range(width)]
    for y in range(width):
        for x in range(width):
            nodes[y][x].x = x
            nodes[y][x].y = y
    unvisited = [nodes[0][0]]
    visited = []
    calculatedWeights[0][0] = 0
    current = Node()
    while len(unvisited) != 0:
        unvisited.sort(key=lambda x : calculatedWeights[x.y][x.x]) #this is clearly the bottleneck but I cba to change the data structure to make it faster, still runs in about 30 seconds
        currentNode = unvisited.pop(0)
        xy = (currentNode.x, currentNode.y)
        currentWeight = calculatedWeights[xy[1]][xy[0]]
        if xy == (width-1, width-1):
            break
        if xy[0] > 0:
            left = (xy[0]-1, xy[1])
            if calculatedWeights[left[1]][left[0]]>currentWeight+weights[left[1]][left[0]]:
                calculatedWeights[xy[1]][xy[0]-1] = currentWeight + weights[left[1]][left[0]]
                unvisited.append(nodes[xy[1]][xy[0]-1])
        if xy[1] > 0:
            up = (xy[0], xy[1]-1)
            if calculatedWeights[up[1]][up[0]]>currentWeight+weights[up[1]][up[0]]:
                calculatedWeights[up[1]][up[0]] = currentWeight + weights[up[1]][up[0]] 
                unvisited.append(nodes[up[1]][up[0]])
        if xy[0] < width-1:
            right = (xy[0]+1, xy[1])
            if calculatedWeights[right[1]][right[0]]>currentWeight+weights[right[1]][right[0]]:
                calculatedWeights[right[1]][right[0]] = currentWeight + weights[right[1]][right[0]]
                unvisited.append(nodes[right[1]][right[0]])
        if xy[1] < width-1:
            down = (xy[0], xy[1]+1)
            if calculatedWeights[down[1]][down[0]]>currentWeight+weights[down[1]][down[0]]:
                calculatedWeights[down[1]][down[0]] = currentWeight + weights[down[1]][down[0]]
                unvisited.append(nodes[down[1]][down[0]])
    path = [['.' for i in range(width)]for j in range(width)]

    # while currentNode.last != (-1, -1):
    #     path[currentNode.y][currentNode.x] = '#'
    #     currentNode = nodes[currentNode.last[1]][currentNode.last[0]]

    # for row in path:
    #     print("".join(row))
    print(calculatedWeights[width-1][width-1])




    
