import math

with open("DAY7.txt", "r") as file:
    crabs = [int(i) for i in file.read().split(",")]
    finalMean = int(sum(crabs)/len(crabs))
    differences = [int(finalMean-num) for num in crabs]
    finalFuel = sum(differences)
    step = -1
    newDifferences = [int(abs(finalMean+step-num)) for num in crabs]
    newFuel = sum(newDifferences)
    while finalFuel>newFuel:
        finalFuel = newFuel
        step-=1
        newDifferences = [int(abs(finalMean+step-num)) for num in crabs]
        print(newDifferences)
        newFuel = sum(newDifferences)
    print(finalFuel)
    print(step)

with open("DAY7.txt", "r") as file:
    crabs = [int(i) for i in file.read().split(",")]
    finalMean = int(sum(crabs)/len(crabs))
    differences = [int((abs(finalMean-num)**2+abs(finalMean-num))/2) for num in crabs]
    finalFuel = sum(differences)
    step = 1
    newDifferences = [int((abs(finalMean+step-num)**2+abs(finalMean+step-num))/2) for num in crabs]
    newFuel = sum(newDifferences)
    while finalFuel>newFuel:
        finalFuel = newFuel
        step+=1
        newDifferences = [int((abs(finalMean+step-num)**2+abs(finalMean+step-num))/2) for num in crabs]
        print(newDifferences)
        newFuel = sum(newDifferences)
    print(finalFuel)
    print(step)