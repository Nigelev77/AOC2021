import functools


with open("DAY3.txt", "r") as file:
    bitsStrings = [str(i).strip() for i in file]
    oneCounts = [0]*(len(bitsStrings[0])-1)
    halfLenCount = len(bitsStrings)/2
    """
    for bits in bitsStrings:
        for i, bit in enumerate(bits):
            if bit == '1':
                oneCounts[i] += 1
    epsilon = ""
    gamma = ""
    for one in oneCounts:
        if one>=halfLenCount:
            gamma += "1"
            epsilon += "0"
        else:
            gamma += "0"
            epsilon += "1"
    epsilonI = int(epsilon, 2)
    gammaI = int(gamma, 2)
    print(epsilonI*gammaI)
"""
    pos = 0
    bitsStrings2 = bitsStrings.copy()
    while len(bitsStrings)>1:
        oneCount = 0
        for bits in bitsStrings:
            if bits[pos] == '1':
                oneCount += 1
        mostPopular = '1'
        if oneCount<(len(bitsStrings)/2):
            mostPopular = '0'
        bitsStrings = list(filter((lambda x : x[pos]==mostPopular), bitsStrings))
        pos+=1
    pos = 0
    while len(bitsStrings2)>1:
        oneCount = 0
        for bits in bitsStrings2:
            if bits[pos] == '1':
                oneCount += 1
        leastPopular = '0'
        if oneCount<(len(bitsStrings2)/2):
            leastPopular = '1'
        bitsStrings2 = list(filter(lambda x : x[pos]==leastPopular, bitsStrings2))
        pos+=1
    o2 = int(bitsStrings[0], 2)
    co2 = int(bitsStrings2[0], 2)
    print(int(bitsStrings[0], 2)*int(bitsStrings2[0], 2))

        
            
        



