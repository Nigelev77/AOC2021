from collections import defaultdict

lengths = [2, 3, 4, 7]
uniqueNumbers = ["cf", "bcdf", "acf", "abcdefg"]
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
letterMap = {"abcefg": "0", "cf":"1", "acdeg":"2", "acdfg":"3", "bcdf":"4", "abdfg":"5", "abdefg":"6", "acf":"7", "abcdefg":"8", "abcdfg":"9"}



def part1():
    with open("DAY8.txt", "r") as file:
        outputNumbers = []
        uniqueOccurrences = defaultdict(lambda : 0)
        for line in file:
            signalOutputs = line.strip().split(" | ")
            signals = [set(i) for i in signalOutputs[0].split(" ")]
            outputs = [set(i) for i in signalOutputs[1].split(" ")]
            currentOutputs = []
            for output in outputs.split(" "):
                if len(output) in lengths:
                    uniqueOccurrences[len(outputs)] += 1
                    currentOutputs.append(output)
            if len(currentOutputs) != 0:
                outputNumbers.append(set(currentOutputs))



with open("DAY8.txt", "r") as file:
    outputNumbers = []
    uniqueOccurrences = defaultdict(lambda : 0)
    total =0
    for line in file:
        mapping = defaultdict(lambda : None)
        for letter in letters:
            mapping[letter] = None
        signalOutputs = line.strip().split(" | ")
        signals = [set(i) for i in signalOutputs[0].split(" ")]
        outputs = [set(i) for i in signalOutputs[1].split(" ")]
        #u = dict([(len(i), [set(i)]) for i in list(filter(lambda x: len(x) in lengths, signals))])
        uniqueSignalCodes = defaultdict(lambda:[])
        for signal in signals:
            count = len(signal)
            uniqueSignalCodes[count].append(signal)
        five = uniqueSignalCodes[5][0]
        two = uniqueSignalCodes[2][0]
        three = uniqueSignalCodes[3][0]
        seven = uniqueSignalCodes[7][0]
        four = uniqueSignalCodes[4][0]
        characterA = min((three - two))
        mapping['a'] = characterA
        characterD = min(five.intersection(uniqueSignalCodes[5][1], uniqueSignalCodes[5][2], four))
        mapping['d'] = characterD

        charactersEDC = set()
        for letters in uniqueSignalCodes[6]:
            charactersEDC.add(min(seven-letters))
        charactersEC = charactersEDC-set(characterD)
        characterE = min(charactersEC-two)
        characterC = min(charactersEC-{characterE})
        mapping['c'] = characterC
        mapping['e'] = characterE
        
        charactersADC = {characterA, characterD, characterC}
        characterF = min(three - charactersADC)
        mapping['f'] = characterF
        characterB = min(four - {characterC, characterD, characterF})
        mapping['b'] = characterB
        characterG = min(set(letters) - {characterA, characterB, characterC, characterD, characterE, characterF})
        mapping['g'] = characterG
        mapping = dict((y,x) for x,y in mapping.items())
        number = ""
        for output in outputs:
            builder = ""
            for char in output:
                builder += mapping[char]
            builder = "".join(sorted(builder))
            number+=letterMap[builder]
        numberI = int(number)
        total+=numberI
    print(total)