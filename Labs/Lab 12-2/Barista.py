from Coffee import Coffee
class Barista():
    MAX_ORDERS = 5
    def __init__(self, baristaName):
        self.name = baristaName
        self.orders = []

    def takeOrder(self):
        desc = input("What drink you want?: ")
        size = input("What size would you like?: ")
        customer = input("What is your name?: ")
        customerOrder = Coffee(size, desc, customer)
        self.orders.append(customerOrder)
        print(customerOrder)

    def isAcceptingOrders(self):
        if len(self.orders)<Barista.MAX_ORDERS:
            return True
        else:
            return False
    def makeDrinks(self):
        for customerOrder in self.orders:
            customerOrder.setCompleted()
            print(customerOrder)
        self.orders = [] # set to empty once done
    def __str__(self):
        return ("My name is", self.name)


