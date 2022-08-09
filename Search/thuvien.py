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
    return result, count


def BinarySearch(arr, number):
    left = 0
    right = arr.__len__()-1
    count = 0
    while left <= right:
        count += 1
        mid = int((left+right)/2)
        if number == arr[mid]:
            return mid, count
        elif number < arr[mid]:
            right = mid-1
        else:
            left = mid+1
    if left > right:
        return -1, count


def BinarySearch_Recursion(arr, number, left, right):
    if left > right:
        return -1
    mid = int((left+right)/2)
    if number == arr[mid]:
        return mid
    else:
        if(number > arr[mid]):
            return BinarySearch_Recursion(arr, number, mid+1, right)
        else:
            return BinarySearch_Recursion(arr, number, left, mid-1)


def InterpolationSearch(arr, number):
    left = 0
    right = arr.__len__()-1
    count = 0
    while left <= right:
        count += 1
        mid = int(Find_Nearest_Mid(arr, left, right, number))
        if mid > right or mid < left:
            return -1, count
        if number == arr[mid]:
            return mid, count
        elif number < arr[mid]:
            right = mid-1
        else:
            left = mid+1
    if left > right:
        return -1, count

    if left > right:
        return -1
    mid = int(Find_Nearest_Mid(arr, left, right, number))
    if number == arr[mid]:
        return mid
    else:
        if(number > arr[mid]):
            return InterpolationSearch_Recursion(arr, number, mid+1, right)
        else:
            return InterpolationSearch_Recursion(arr, number, left, mid-1)
