signalGrid = []
uniqueAntinodes = 0
uniqueCoordinates = set()

def calculateDiff(pointA, pointB):
    return (pointB[0] - pointA[0], pointB[1] - pointA[1])

def isInBounds(node):
    x = node[0]
    y = node[1]
    return x >= 0 and x < 50 and y >= 0 and y < 50

def isUnique(node):
    return not node in uniqueCoordinates

file = open('C:\\Users\\rober\\Documents\\advent\\day8input.txt', 'r')
lines = file.readlines()
for line in lines:
    frequencies = list(line.strip())
    signalGrid.append(frequencies)
    
##for x in range(len(signalGrid)):
##    for y in range(len(signalGrid[x])):
##        if signalGrid[x][y] == '.':
##            continue
##        else:
##            pointA = (x,y)
##            currentFrequency = signalGrid[x][y]
##            nextRow = x + 1
##            while (nextRow < len(signalGrid)):
##                for col in range(len(signalGrid[nextRow])):
##                    if signalGrid[nextRow][col] == currentFrequency:
##                        pointB = (nextRow, col)
##                        slope = calculateDiff(pointA, pointB)
##                        antinode1 = calculateDiff(slope, pointA)
##                        antinode2 = (pointB[0]+slope[0], pointB[1]+slope[1])
##                        if isInBounds(antinode1) and isUnique(antinode1):
##                            uniqueCoordinates.add(antinode1)
##                            uniqueAntinodes += 1
##                        if isInBounds(antinode2) and isUnique(antinode2):
##                            uniqueCoordinates.add(antinode2)
##                            uniqueAntinodes += 1
##                    else:
##                        continue
##                nextRow += 1
            
##print(uniqueAntinodes)


#part 2
for x in range(len(signalGrid)):
    for y in range(len(signalGrid[x])):
        if signalGrid[x][y] == '.':
            continue
        else:
            pointA = (x,y)
            currentFrequency = signalGrid[x][y]
            nextRow = x + 1
            while (nextRow < len(signalGrid)):
                for col in range(len(signalGrid[nextRow])):
                    if signalGrid[nextRow][col] == currentFrequency:
                        pointB = (nextRow, col)
                        if isUnique(pointA):
                            uniqueCoordinates.add(pointA)
                            uniqueAntinodes += 1
                        if isUnique(pointB):
                            uniqueCoordinates.add(pointB)
                            uniqueAntinodes += 1
                            
                        slope = calculateDiff(pointA, pointB)
                        antinode1 = calculateDiff(slope, pointA)
                        while(isInBounds(antinode1)):
                            if isUnique(antinode1):
                                uniqueCoordinates.add(antinode1)
                                uniqueAntinodes += 1
                            antinode1 = calculateDiff(slope,antinode1)
                            
                        antinode2 = (pointB[0]+slope[0], pointB[1]+slope[1])
                        while(isInBounds(antinode2)):
                            if isUnique(antinode2):
                                uniqueCoordinates.add(antinode2)
                                uniqueAntinodes += 1
                            antinode2 = (antinode2[0]+slope[0], antinode2[1]+slope[1])
                    else:
                        continue
                nextRow += 1

print(uniqueAntinodes)
