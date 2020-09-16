# Michelle Liang, liangmic@usc.edu
# ITP 115, Spring 2020
# Final Project

class Diner(object):
    STATUSES = ["seated", "ordering", "eating", "paying", "leaving"]
    def __init__(self, name):
        self.name = name
        self.order = []
        self.status = 0

    def getName(self):
        return self.name

    def getOrder(self):
        return self.order

    def getStatus(self):
        return Diner.STATUSES[self.status]

    def updateStatus(self):
        if self.status <= 3:
            self.status = self.status + 1

    def addToOrder(self, menuItem):
        self.order.append(menuItem)

    def printOrder(self):
        print(self.name, "ordered:")
        for menuItem in self.order:
            print("-", menuItem)

    def calculateMealCost(self):
        count = 0
        for menuItem in self.order:  # adds up all the costs of each individual menu item
            count+=float(menuItem.price)
        return count

    def __str__(self):
        result = "Diner " + self.name + " is currently " + Diner.STATUSES[self.status]
        return result


