from os import system
import menu as m

menu = 'a'
while menu != 0:
    menu = m.ChonMenu()
    m.XuLyMenu(menu)
system('cls')
