# Michelle Liang, liangmic@usc.edu
# ITP 115, Spring 2020
# Lab 8-1

def temperatureConverter(conversionType, inputTemperature):
    if inputTemperature.isdigit():
        inputTemperature = float(inputTemperature)
        tempisnum = True
    else:
        print("Invalid temperature or conversion code")
        return "not"

    if not conversionType.isdigit():
        print("Invalid conversion code")
        return "not"

    if int(conversionType) == 1:
        ans = (inputTemperature - 32) * (5 / 9)
        return ans
    if int(conversionType) == 2 :
        ans = (inputTemperature * (9 / 5)) + 32
        return ans
    else:
        print("Invalid conversion code")
        return "not"


def wantsToContinue():
    loop = True
    while loop:
        choice = input("Repeat? (y/n) ")
        if choice.lower() == "n":
            return False
        if choice.lower() == "y":
            return True


def main():
    contin = True
    while contin == True:
        type = input("Enter 1 for F->C, 2 for C->F: ")
        temp = input("Enter input temperature: ")
        final = temperatureConverter(type, temp)
        if final == "not":
            contin = wantsToContinue()
        else:
            contin = False
            print("The temperature is " + str(final) + " degrees", end=" ")
            if type == 1:
                print("Celcius")
            else:
                print("Fahrenheit")
    if contin == False:
        print("Bye!")

main()
