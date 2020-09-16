# Michelle Liang, liangmic@usc.edu
# ITP 115, Spring 2020
# Final Project

# Description:
# Creating the class that represents a single item that can be ordered off the menu

class MenuItem():
    # constructor
    def __init__(self, name, type, price, descr):
        self.name = name
        self.type = type
        self.price = price
        self.description = descr

    # get methods
    def getName(self):
        return self.name

    def getType(self):
        return self.type

    def getPrice(self):
        return self.price

    def getDescription(self):
        return self.description

    def __str__(self):
        result = self.name + " (" + self.type + "): $" + str(self.price) + "\n\t" + self.description
        return result




