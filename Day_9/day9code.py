def blockCompact(blocks):
    start = 0
    end = len(blocks)-1
    while start < end:
        if blocks[start] != -1:
            start +=1
            continue
        if blocks[end] == -1:
            end -= 1
            continue
        blocks[start] = blocks[end]
        blocks[end] = -1
    return blocks

def checksum(arr):
    result = 0
    for index in range(len(arr)):
        if arr[index] != -1:
            result += index * arr[index]
    return result

file = open('day9input.txt', 'r')
diskmap = file.readlines()[0].strip()
blocks = []
locations = []
fileId = 0
for (index, spaceTaken) in enumerate(map(int,diskmap)):
    if index % 2 == 0:
        blocks += [fileId] * spaceTaken
        locations.append((fileId, spaceTaken))
        fileId += 1
    else:
        blocks += [-1] * spaceTaken

compactBlock = blockCompact(blocks.copy())
checksums = checksum(compactBlock)
print(checksums)

reversedLocations = reversed(locations)
for idAndSize in reversedLocations:
    fileId = idAndSize[0]
    fileSize = idAndSize[1]
    freeSpace = 0
    fileIndex = blocks.index(fileId)
    for index in range(fileIndex):
        if blocks[index] != -1:
            freeSpace = 0
            continue
        freeSpace += 1
        if freeSpace >= fileSize:
            for space in range(fileSize):
                blocks[index-space] = fileId
                blocks[fileIndex+space] = -1
            break

checksum2 = checksum(blocks)
print(checksum2)
