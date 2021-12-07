from collections import defaultdict

import time
t0 = time.time()
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
    print(time.time()-t0)
    print(total)

days = 256

# 0 days, 1 days, 2 days
t0 = time.time()
fish = [0, 0, 0, 0, 0, 0, 0, 0, 0]
raw = [int(line) for line in open("DAY6.txt").readline().split(',')]
for f in raw:
  fish[f] = fish[f] + 1  
for d in range(days):
  births = fish[0]
  for i in range(1, len(fish)):
    fish[i - 1] = fish[i]
  fish[6] = fish[6] + births
  fish[8] = births
print(time.time()-t0)
print(f"In {d+1} days there will be {sum(fish)} fish")