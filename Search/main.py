from os import system
from menu import MenuClass
import numpy as np
choice = '123'
menu = MenuClass()
while choice != 0:
    choice = menu.ChonMenu()
    menu.XuLyMenu(choice)
system('cls')

# a = np.array([1,9, 6, 4, 2 ,5, 7, 0, 8, 3])

# def LinearSearch(array, number):
#     result = -1
#     i = 0
#     # count = 0
#     length = array.__len__()
#     while i < length:
#         # count += 1
#         if array[i] == number:
#             result = i
#             break
#         else:
#             i += 1
#     return result
# n = int(input("Xin hãy nhập số cần tìm: "))
# result = LinearSearch(a, n)
# if result == -1:
#      print('Không tìm thấy số ' + str(n)+' trong mảng!')
# else:
#     print('Số '+str(n)+' nằm ở vị trí '+str(result+1))