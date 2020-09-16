# Michelle Liang, liangmic@usc.edu
# ITP 115, Spring 2020
# Lab 2-1


# Description:
# Taking the user's input for coffee order and stating it in a sentence, using if/else

def main():
    size = input("What size coffee do you want? S,M,L ")
    rand = input("Would you like a random temperature? (y/n) ")

    if rand == "n":
        temp = input("What temperature would you like (in degrees Fahrenheit)? ")

    beans = input("What type of beans / blend would you like? ")
    cream = input("Would you like room for cream? (y/n) ")


#cycle thru if/else statements for size, temp, and cream
    #size
    if size == "S":
        size = "small"
    elif size == "M":
        size = "medium"
    elif size == "L":
        size = "large"

    else:                    #checking lowercase too
        if size == "s":
            size = "small"
        elif size == "m":
            size = "medium"
        elif size == "l":
            size = "large"

    #random temp
    import random
    if rand == "y":
        temp = random.randrange(70, 200)

    #temp
    if rand == "n":
        temp = int(temp)         #convert temp to integer
        if temp > 90:
            temp = str(temp)
            temp = "hot"
        else:
            temp = "cold"
    else:
        if temp > 90:
            temp = str(temp)
            temp = "hot"
        else:
            temp = "cold"
    #cream
    if cream == "n":
        cream = "no "
    if cream == "y":
        cream = ""

#print their order
    print("You ordered a " + size + " " + temp + " " + beans + " coffee with " + cream + "cream.")

main()