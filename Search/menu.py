from os import system


features = ("Thoát chương trình",
            "Nhập dữ liệu",
            "Xem dữ liệu")


def XuatMenu():
    print('============================== HỆ THỐNG MENU ==============================')
    for feature in features:
        print(str(features.index(feature))+". "+feature)
    print('===========================================================================')


def ChonMenu(soMenu=len(features)-1):
    menu = ""
    while True:
        system('cls')
        XuatMenu()
        temp = input(
            "Xin hãy nhập 1 số [0.."+str(soMenu)+"] để chọn chức năng tương ứng: ")
        try:
            menu = int(temp)
            if 0 <= menu and menu <= soMenu:
                break
        except:
            print("Nhập không hợp lệ! Xin hãy thử lại!")
            input("Nhấn phím Enter để tiếp tục")
    return menu


def XuLyMenu(menu):
    system('cls')
    # region Case 0
    if features[menu] == "Thoát chương trình":
        print("Thoát chương trình")
    # endregion

    # region Case 1
    elif features[menu] == "Nhập dữ liệu":
        print("Nhập dữ liệu")
    # endregion

    # region Case 2
    elif features[menu] == "Xem dữ liệu":
        print("Xem dữ liệu")
    # endregion

    # region Default Case
    else:
        print("Chức năng này chưa được hỗ trợ")
    # endregion
    input("Nhấn phím enter để tiếp tục!")
