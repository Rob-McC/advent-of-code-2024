def calibrationOperations(value, arr, index, target):
    if value == target and index == len(arr) - 1:
        return value
    elif index < len(arr) - 1:
        index += 1
        return (calibrationOperations(value * arr[index], arr, index, target) +
                calibrationOperations(value + arr[index], arr, index, target) +
                calibrationOperations(int(str(value) + str(arr[index])), arr, index, target))
    else:
        return 0


totalCalibration = 0
file = open('C:\\Users\\rober\\Documents\\advent\\day7input.txt', 'r')
lines = file.readlines()
for line in lines:
    equation = line.strip().split(" ")
    target = int(equation[0].split(":")[0])
    operands = list(map(int, equation[1:]))
    result = calibrationOperations(operands[0], operands, 0, target)
    if result > 0:
        totalCalibration += target
print(totalCalibration)
# getting num:97902811429005
# solution is 97902809384118
# issue was that some equations reached the solution before evaluating ALL operands
# I added check to ensure index is at the end of the array to fix this
