from collections import defaultdict
import copy
import time

with open("DAY14.txt", "r") as file:
    template = file.readline().strip()
    file.readline()
    rules = dict(i.split(" -> ") for i in file.read().split("\n"))
    t0 = time.time()
    occurrences = defaultdict(lambda: 0)
    lastInsertion = ""
    for pos in range(len(template)-1):
        pair = template[pos:pos+2]
        occurrences[pair] += 1
    lastInsertion = pair
    firstPair = ""
    lastPair = ""
    for step in range(40):
        pairs = list(occurrences.keys())
        temp = copy.copy(occurrences)
        for i in range(len(pairs)):
            pair = pairs[i]
            if i == 0:
                firstPair = pair
            elif i == len(pairs)-1:
                lastPair = pair
            if pair in rules.keys():
                inserted = rules[pair]
                l = pair[0] + inserted
                r = inserted + pair[1]
                occurrences[l] += temp[pair]
                occurrences[r] += temp[pair]
                occurrences[pair] -= temp[pair]
                if pair == lastInsertion:
                    lastInsertion = r
                if i == 0:
                    firstPair = l
                elif i == len(pairs)-1:
                    lastPair = r
    chars = defaultdict(lambda:0)
    for pair in occurrences.keys():
        chars[pair[0]] += occurrences[pair]
    chars[lastInsertion[1]] += 1
    print(time.time()-t0)
    print(max(chars.values()) - min(chars.values()))