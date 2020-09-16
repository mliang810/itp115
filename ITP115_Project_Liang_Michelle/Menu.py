# Michelle Liang, liangmic@usc.edu
# ITP 115, Spring 2020
# Final Project

from MenuItem import MenuItem
class Menu(object):
    MENU_ITEM_TYPES = ["Drink", "Appetizer", "Entree", "Dessert"]
    def __init__(self, fileName):
        self.menuItemDictionary = dict()

        # dict. with menu item types (keys), empty dictionary
        for type in self.MENU_ITEM_TYPES:
            self.menuItemDictionary[type] = list()

        # read in, add items to dict.
        fileIn = open(fileName, "r")
        for line in fileIn:
            lineDone = line.strip().split(",")
            if lineDone[1] == self.MENU_ITEM_TYPES[0]:
                temp = MenuItem(lineDone[0], lineDone[1], lineDone[2], lineDone[3])
                self.menuItemDictionary[Menu.MENU_ITEM_TYPES[0]].append(temp)

            if lineDone[1] == self.MENU_ITEM_TYPES[1]:
                temp = MenuItem(lineDone[0], lineDone[1], lineDone[2], lineDone[3])
                self.menuItemDictionary[Menu.MENU_ITEM_TYPES[1]].append(temp)

            if lineDone[1] == self.MENU_ITEM_TYPES[2]:
                temp = MenuItem(lineDone[0], lineDone[1], lineDone[2], lineDone[3])
                self.menuItemDictionary[Menu.MENU_ITEM_TYPES[2]].append(temp)

            if lineDone[1] == self.MENU_ITEM_TYPES[3]:
                temp = MenuItem(lineDone[0], lineDone[1], lineDone[2], lineDone[3])
                self.menuItemDictionary[Menu.MENU_ITEM_TYPES[3]].append(temp)

        fileIn.close()

    def getMenuItem(self, type, index):
        return self.menuItemDictionary[type][index]

    def printMenuItemsByType(self, type):
        # Print a header with the type of menu items, followed by a numbered list of all the menu items of that type.
        print("\n------" + str(type.upper()) + "------")
        count = 0
        for item in self.menuItemDictionary[type.title()]:
            count += 1
            print(str(count) + ") ", item)

    def getNumMenuItemsByType(self, type):
        # returns an integer representing the number of MenuItems under the input type
        return len(self.menuItemDictionary[type])


