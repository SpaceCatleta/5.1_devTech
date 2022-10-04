

def counter_sort(intArray) -> list:
    minVal, maxVal = intArray[0], intArray[0]

    for val in intArray:
        minVal = minVal if val >= minVal else val
        maxVal = maxVal if val <= maxVal else val

    size = maxVal - minVal + 1
    counterArray = [0] * size

    for val in intArray:
        counterArray[val - minVal] += 1

    newArray = [0] * len(intArray)
    item = 0
    counterItem = 0

    for counter in counterArray:
        if counter == 0:
            counterItem += 1
            continue

        for i in range(counter):
            newArray[item] = counterItem + minVal
            item += 1

        counterItem += 1

    return newArray


def sort2(intArray) -> list:
    size = len(intArray)
    start, end = 0, size-1

    while start < end:
        minIndex, maxIndex = start, start

        for i in range(start, end + 1):
            minIndex = minIndex if intArray[minIndex] < intArray[i] else i
            maxIndex = maxIndex if intArray[maxIndex] > intArray[i] else i

        intArray = change_values(intArray, minIndex, start)
        intArray = change_values(intArray, maxIndex, end)
        start += 1
        end -= 1

    return intArray


def change_values(array, index1, index2):
    val = array[index1]
    array[index1] = array[index2]
    array[index2] = val
    return array
