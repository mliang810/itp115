height = int(input("How tall is the triangle you wish to print? Please enter an integer: "))
line = 0
carrot = "^"
numSpaces = 2 * (height - 1)


while line < height:
    print(" " * numSpaces, end = "")
    print(carrot)
    carrot = "^ " + carrot + " ^"
    line +=1
    numSpaces -= 2

