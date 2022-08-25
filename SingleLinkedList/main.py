from os import system
from menu import MenuClass
import numpy as np
choice = '123'
menu = MenuClass()
while choice != 0:
    choice = menu.ChonMenu()
    menu.XuLyMenu(choice)
system('cls')

# from singlyLInkedList import SinglyLinkedList

# words = SinglyLinkedList()
# words.Append("a")
# words.Append("b")
# words.Append("c")
# for word in words.iter():
#     print(word)