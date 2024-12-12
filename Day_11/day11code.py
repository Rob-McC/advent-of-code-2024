def calculateStoneTransformation(stone):
    if int(stone) == 0:
        return [str(1)]
    elif len(stone) % 2 == 0:
        midpoint = int(len(stone)/2)
        return [str(int(stone[:midpoint])),str(int(stone[midpoint:]))]
    else:
        return [str(int(stone)*2024)]

def findCountForGen(blinks, targetBlinks, existingStones, stone):
    if blinks == targetBlinks:
        return 1
    if (stone,blinks) in existingStones: #going to hit same generation at some point
        return existingStones[(stone,blinks)]
    stoneCount = 0
    nextGen = calculateStoneTransformation(stone)
    for newStone in nextGen:
        stoneCount += findCountForGen(blinks+1, targetBlinks, existingStones, newStone)
    existingStones[(stone,blinks)] = stoneCount
    return stoneCount

file = open('day11input.txt', 'r')
lines = file.readlines()
initialStones = []
gen25StoneCounts = []
gen75StoneCounts = []
for line in lines:
    initialStones = line.strip().split(" ")

print(initialStones)
existingStoneGen = {}
repeatGen = {}
for stone in initialStones:
    #pt 1
    stoneCountAfter25 = findCountForGen(0, 25, existingStoneGen, stone)
    gen25StoneCounts.append(stoneCountAfter25)
    #pt 2
    stoneCountAfter75 = findCountForGen(0, 75, repeatGen, stone)
    gen75StoneCounts.append(stoneCountAfter75)

print("Count for part 1: " + str(sum(gen25StoneCounts)))
print("Count for part 2: " + str(sum(gen75StoneCounts)))
