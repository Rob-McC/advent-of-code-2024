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
file = open('day7input.txt', 'r')
lines = file.readlines()
for line in lines:
    equation = line.strip().split(" ")
    target = int(equation[0].split(":")[0])
    operands = list(map(int, equation[1:]))
    result = calibrationOperations(operands[0], operands, 0, target)
    if result > 0:
        totalCalibration += target
print(totalCalibration)
