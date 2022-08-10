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


def BubbleSort(arr):
    length = arr.__len__()-1
    for i in range(length, 0, -1):
        for j in range(i):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp

def InsertionSort(arr):
    length = arr.__len__()
    for index in range(1, length):
        search_index = index
        insert_value = arr[index]
        while search_index > 0 and insert_value < arr[search_index-1]:
            arr[search_index] = arr[search_index-1]
            search_index -= 1
        arr[search_index] = insert_value
