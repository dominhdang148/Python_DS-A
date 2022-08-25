import numpy as np


def Find_Nearest_Mid(array, left, right, value):
    return left+((right-left))/(array[right]-array[left])*(value-array[left])


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



