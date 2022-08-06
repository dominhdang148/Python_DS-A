import numpy as np


def ReadFile(path):
    line = "123"
    with open(path, 'r') as fileReader:
        while ((line := fileReader.readline()) != ""):
            str = line.split(' ')
            arr = np.array(str)
    return arr


def PrintArray(arr):
    s = ""
    for x in arr:
        s += str(x)+'\t'
    print(s)


def LinearSearch(array, number):
    result = -1
    i = 0
    count = 0
    length = array.__len__()
    while i < length:
        count += 1
        if array[i] == number:
            result = i
            break
        else:
            i += 1
    return result,count
