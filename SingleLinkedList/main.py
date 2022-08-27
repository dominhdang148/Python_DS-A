# from os import system
# from menu import MenuClass
# import numpy as np
# choice = '123'
# menu = MenuClass()
# while choice != 0:
#     choice = menu.ChonMenu()
#     menu.XuLyMenu(choice)
# system('cls')

from singlyLInkedList import SinglyLinkedList

words = SinglyLinkedList()
# words.append("a")
# words.append("b")
# words.append("c")

# for word in words.iter():
#     print(word)

# print("The size of the current list: {}".format(words.size))
print("Inserting 'y' in the first line")
words.insert_after('y', 't')

for word in words.iter():
    print(word)
print("The size of the current list: {}".format(words.size))