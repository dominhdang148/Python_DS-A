from os import system
import numpy as np
import thuvien as lib


class MenuClass:
    menuList = (
        'Thoát chương trình',
        'Nhập dữ liệu',
        'Xuất dữ liệu',
        'Tìm kiếm tuyến tính (Linear Search)',
        'Tìm kiếm nhị phân (Binary Search)',
        'Tìm kiếm nội suy (Interpolation Search)'
    )
    arr = np.array([])

    def __init__(self):
        pass

    def XuatMenu(self):
        print("============================= HỆ THỐNG MENU =============================")
        for choice in self.menuList:
            print(str(self.menuList.index(choice)) + ". "+choice)
        print("=========================================================================")

    def ChonMenu(self, soMenu=len(menuList)-1):
        menu = ""
        while True:
            system('cls')
            self.XuatMenu()
            temp = input(
                "Xin hãy chọn một số [0.."+str(soMenu)+"] để chọn chức năng tương ứng: ")
            try:
                menu = int(temp)
                if 0 <= menu and menu <= soMenu:
                    break
            except:
                input("Nhập không hợp lệ! Nhấn phím Enter để tiếp tục")
        return menu

    def XuLyMenu(self, menu):

        system("cls")

        # region Case 0
        if self.menuList[menu] == "Thoát chương trình":
            print("Thoát chương trình")
        # endregion

        # region Case 1
        elif self.menuList[menu] == "Nhập dữ liệu":
            temp = lib.ReadFile('file.txt')
            self.arr = temp.astype(int)
            print("Nhập dữ liệu")
            print("Nhập dữ liệu thành công! Mảng số nguyên sau khi nhập")
            lib.PrintArray(self.arr)
        # endregion

        # region Case 2
        elif self.menuList[menu] == "Xuất dữ liệu":
            print("Mảng số nguyên hiện hành")
            lib.PrintArray(self.arr)
        # endregion

        # region Case 3
        elif self.menuList[menu] == "Tìm kiếm tuyến tính (Linear Search)":
            try:
                n = int(input("Xin hãy nhập số cần tìm: "))
                result, count = lib.LinearSearch(self.arr, n)
                if result == -1:
                    print('Không tìm thấy số ' + str(n)+' trong mảng!')
                else:
                    print('Số '+str(n)+' nằm ở vị trí '+str(result))
                    print("Thuật toán thực hiện trong "+str(count)+" bước")
                    print("Mảng số nguyên hiện hành")
                    lib.PrintArray(self.arr)
            except:
                print("Nhập không hợp lệ! Xin hãy nhập lại")
        # endregion

        # region Case 4
        elif self.menuList[menu] == "Tìm kiếm nhị phân (Binary Search)":
            n = int(input("Xin hãy nhập số cần tìm: "))
            print(
                "Thuật toán tìm kiếm này yêu cầu phải sắp xếp mảng sổ nguyên theo chiều tăng dần")
            self.arr = np.sort(self.arr)
            result, count=lib.BinarySearch(self.arr, n)
            # result = lib.BinarySearch_Recursion(
            #     self.arr, n, 0, self.arr.__len__()-1)
            if result == -1:
                print('Không tìm thấy số ' + str(n)+' trong mảng!')
            else:
                print('Số '+str(n)+' nằm ở vị trí '+str(result))
            print("Thuật toán thực hiện trong "+str(count)+" bước")
            print("Mảng số nguyên hiện hành")
            lib.PrintArray(self.arr)
        # endregion

        # region Case 5
        elif self.menuList[menu] == "Tìm kiếm nội suy (Interpolation Search)":
            n = int(input("Xin hãy nhập số cần tìm: "))
            print(
                "Thuật toán tìm kiếm này yêu cầu phải sắp xếp mảng sổ nguyên theo chiều tăng dần")
            self.arr = np.sort(self.arr)
            result, count=lib.InterpolationSearch(self.arr, n)
            # result = lib.BinarySearch_Recursion(
            #     self.arr, n, 0, self.arr.__len__()-1)
            if result == -1:
                print('Không tìm thấy số ' + str(n)+' trong mảng!')
            else:
                print('Số '+str(n)+' nằm ở vị trí '+str(result))
            print("Thuật toán thực hiện trong "+str(count)+" bước")
            print("Mảng số nguyên hiện hành")
            lib.PrintArray(self.arr)
        # endregion

        # region Default
        else:
            print("Chương trình chưa hỗ trợ chức năng này")
        input("Nhấn phím Enter để tiếp tục")
        # endregion
