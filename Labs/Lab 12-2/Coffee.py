class Coffee():
    STATUSES = ["ordered", "completed"]
    def __init__(self, sizeIn, descIn, customerIn):
        self.size = sizeIn
        self.desc = descIn
        self.customer = customerIn
        self.statusIndex = 0

    def setCompleted(self):
        self.statusIndex = 1

    def __str__(self):
        msg = (self.desc + " for " + self.customer + " (" + self.STATUSES[self.statusIndex] + ")")
        return msg


