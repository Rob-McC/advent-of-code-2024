def startSearch(trails, startPoint, unique9s, ratings):
    row = startPoint[0]
    col = startPoint[1]
    findTrailheadPaths((row+1,col),startPoint,trails,startPoint,unique9s, ratings)
    findTrailheadPaths((row-1,col),startPoint,trails,startPoint,unique9s, ratings)
    findTrailheadPaths((row,col+1),startPoint,trails,startPoint,unique9s, ratings)
    findTrailheadPaths((row,col-1),startPoint,trails,startPoint,unique9s, ratings)

def validStep(trails, currentStep, prevStep):
    return (trails[currentStep[0]][currentStep[1]] - trails[prevStep[0]][prevStep[1]]) == 1

def findTrailheadPaths(currentStep, prevStep, trails, startPoint, trailheadUnique9s, ratings):
    row = currentStep[0]
    col = currentStep[1]
    if (row < 0 or row >= 47) or (col < 0 or col >= 47) or not validStep(trails,currentStep,prevStep):
        return None
    elif trails[currentStep[0]][currentStep[1]] == 9:
        trailheadUnique9s[startPoint].add((currentStep[0],currentStep[1]))
        ratings[startPoint] += 1        
        return None
    else:
        findTrailheadPaths((row+1,col),currentStep,trails,startPoint,trailheadUnique9s,ratings)
        findTrailheadPaths((row-1,col),currentStep,trails,startPoint,trailheadUnique9s,ratings)
        findTrailheadPaths((row,col+1),currentStep,trails,startPoint,trailheadUnique9s,ratings)
        findTrailheadPaths((row,col-1),currentStep,trails,startPoint,trailheadUnique9s,ratings)

file = open('day10input.txt', 'r')
lines = file.readlines()
trails = []
for line in lines:
    trails.append(list(map(int,line.strip())))

trailheads = []
for i in range(len(trails)):
    for j in range(len(trails[i])):
        if trails[i][j] == 0:
            trailheads.append((i,j))

trailheadScores = dict(map(lambda i: (trailheads[i], 0), range(len(trailheads))))
trailheadUnique9s = dict(map(lambda i: (trailheads[i], set()), range(len(trailheads))))
trailheadRatings = dict(map(lambda i: (trailheads[i], 0), range(len(trailheads))))
for trailhead in trailheads:
    #call function to iterate over
    startSearch(trails, trailhead, trailheadUnique9s,trailheadRatings)
    # add length of unique 9s set to Scores dict
    trailheadScores[trailhead] = len(trailheadUnique9s.get(trailhead))

print(sum(trailheadScores.values()))
print(sum(trailheadRatings.values()))
