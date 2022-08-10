from os import system
import numpy as np
import thuvien as lib


class MenuClass:
    menuList = (
        'Thoát chương trình',
        'Nhập dữ liệu',
        'Xuất dữ liệu',
        'Sắp xếp nổi bọt (Bubble Sort)',
        'Sắp xếp chèn (Insertion Sort)',
        'Chức năng 5'
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
        elif self.menuList[menu] == "Sắp xếp nổi bọt (Bubble Sort)":
            print("Mảng trước khi sắp xếp:")
            lib.PrintArray(self.arr)
            lib.BubbleSort(self.arr)
            print("Mảng sau khi sắp xếp: ")
            lib.PrintArray(self.arr)
        # endregion

        # region Case 4
        elif self.menuList[menu] == "Sắp xếp chèn (Insertion Sort)":
            print("Mảng trước khi sắp xếp:")
            lib.PrintArray(self.arr)
            lib.InsertionSort(self.arr)
            print("Mảng sau khi sắp xếp: ")
            lib.PrintArray(self.arr)
        # endregion

        # region Case 5
        elif self.menuList[menu] == "Chức năng 5":
            print("Chức năng 5")
        # endregion

        # region Default
        else:
            print("Chương trình chưa hỗ trợ chức năng này")
        input("Nhấn phím Enter để tiếp tục")
        # endregion
