# Michelle Liang, liangmic@usc.edu
# ITP 115, Spring 2020
# Final Project

from Diner import Diner
from Menu import Menu

class Waiter(object):
    def __init__(self, menu):
        self.menu = menu
        self.diners = []

    def addDiner(self, diner):
        self.diners.append(diner)

    def getNumDiners(self):
        return len(self.diners)

    def printDinerStatuses(self):
        for index in range(5):
            print("Diners who are " + Diner.STATUSES[index] + ":")
            for diner in self.diners:
                if diner.getStatus() == Diner.STATUSES[index]:
                    print("\t" + str(diner))

    def takeOrders(self):
        for diner in self.diners:
            if diner.getStatus() == "ordering":
                for type in self.menu.MENU_ITEM_TYPES: #diner will order exactly one item of each type
                    self.menu.printMenuItemsByType(type)
                    order = input(diner.getName() + ", please select a " + str(type) + " menu item number. ")

                    keepGoing = True
                    while keepGoing:
                        if not order.isdigit():
                            print("Invalid. Please try again")
                            order = input(diner.getName() + ", please select a " + str(type) + " menu item number. ")
                        elif int(order) <= 0 or int(order) > self.menu.getNumMenuItemsByType(type): # range check
                            print("Invalid order. Please try again")
                            order = input(diner.getName() + ", please select a " + str(type) + " menu item number. ")
                        else:
                            keepGoing = False # quit loop

                    diner.addToOrder(self.menu.getMenuItem(type, int(order)-1))
                print("")
                diner.printOrder()

    def ringUpDiners(self):
        for diner in self.diners:
            if diner.getStatus() == "paying":
                temp = diner.calculateMealCost()
                print("\n" + str(diner.name) + ", your meal cost $" + str(temp) + ".")

    def removeDiners(self):
        for num in range(len(self.diners)-1,-1,-1): # count down
            if self.diners[num].getStatus() == "leaving":
                print("\nThank you for dining with us " + self.diners[num].getName() + ". Come again soon! :)")
                del self.diners[num] # takes them out

    def advanceDiners(self):
        self.printDinerStatuses()
        self.takeOrders()
        self.ringUpDiners()
        self.removeDiners()
        for diner in self.diners:
            diner.updateStatus()

