import itertools
from collections import defaultdict
"""
def part1():
    for day in range(1, 257):
        for family in lanternFish:
            for p in range(len(family)):
                parent = family[p]
                if parent+1 == day:
                    family.append(parent+9)
                    family[p] = parent+7
"""


with open("DAY6.txt", "r") as file:
    lanternFish = [int(i) for i in file.read().split(",")]
    days = defaultdict(lambda: 0)
    total = len(lanternFish)
    for fish in lanternFish:
        days[fish+1] += 1
    for day in range(1, 257):
        days[day+9] += days[day]
        days[day+7] += days[day]
        total += days[day]
    print(days)
    print(total)