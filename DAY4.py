import re

def checkRow(board):
    count = 0
    for row in board:
        for num in row:
            if num[1]:
                count += 1
        if count==5:
            return True
        count = 0

    return False


def checkCol(board):
    for i in range(5):
        count = 0
        for j in range(5):
            if board[j][i][1]:
                count += 1
        if count == 5:
            return True
        count = 0
    return False

def check(board):
    if checkRow(board) or checkCol(board):
        return False
    else:
        return True

def calculateWinner(board, calledNum):
    unmarkedSum = 0
    for row in board:
        for num in row:
            if not num[1]:
                unmarkedSum+=num[0]
    for row in board:
        print(row)
    print(unmarkedSum)
    print(unmarkedSum*calledNum)

with open("DAY4.txt", "r") as file:
    numbersSeq = [int(i) for i in file.readline().split(",")]
    boards = []
    file.readline()
    for board in range(100):
        rows = list(list(re.split(r'\s{1,}', file.readline().strip())) for j in range(5))
        newBoard = [[[int(num), False] for num in row] for row in rows]
        boards.append(newBoard)
        file.readline()

    count = 0
    lastWinner = []
    lastCalled = 0
    while len(numbersSeq)>0:
        nextNum = numbersSeq.pop(0)
        for board in boards:
            for row in board:
                for num in row:
                    if nextNum == num[0]:
                        num[1] = True
        

        for board in boards:
            if checkRow(board):
                lastWinner = board
                lastCalled = nextNum
            elif checkCol(board):
                lastWinner = board
                lastCalled = nextNum

        boards = list(filter(check, boards))
    calculateWinner(lastWinner, lastCalled)
