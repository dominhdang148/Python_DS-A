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


def Partition(arr, left, right):
    pivot = arr[left]
    pivot_index = left
    index_last = right

    less_than_pivot = index_last
    greater_than_pivot = left+1

    while True:

        # Tìm phần tử đang nằm sai vị trí so với biến pivot:
        while arr[greater_than_pivot] < pivot and greater_than_pivot < right:
            greater_than_pivot += 1
        while arr[less_than_pivot] > pivot and less_than_pivot >= left:
            less_than_pivot -= 1
        # Thực hiện đổi chỗ các phần tử đang bị sai vị trí về dúng vị trí:
        if greater_than_pivot < less_than_pivot:
            arr[greater_than_pivot], arr[less_than_pivot] = arr[less_than_pivot], arr[greater_than_pivot]
        else:
            break
    
    # Đổi chỗ cho biến làm chuẩn pivot về đúng vị trí
    arr[pivot_index] = arr[less_than_pivot]
    arr[less_than_pivot] = pivot
    return less_than_pivot


def QuickSort(arr, left, right):
    if right-left <= 0:
        return
    else:
        partition_index = Partition(arr, left, right)
        QuickSort(arr, left, partition_index-1)
        QuickSort(arr, partition_index+1, right)
