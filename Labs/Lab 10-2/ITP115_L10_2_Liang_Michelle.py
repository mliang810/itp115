# Michelle Liang, liangmic@usc.edu
# ITP 115, Spring 2020
# Lab 10-2

def readFile(fileName):
    fileIn = open(fileName, "r")
    output = []
    for line in fileIn:
        person = line.split(",")
        if int(person[3])<30:
            output.append(person[0])
    fileIn.close()
    return output

def writeFile(outputList, fileName):
    fileOut = open(fileName, "w")
    for names in outputList:
        print(names, file=fileOut)
    print(len(outputList), "names were written to", fileName)

def main():
    fileNameIn = input("Enter the name of the CSV file you wish to read in: ")
    fileNameOut = input("Enter the name of the file you wish to write to: ")
    if fileNameIn.strip() == "":
        outputList = readFile("people.csv")
    else:
        outputList = readFile(fileNameIn)

    if fileNameOut.strip() == "":
        writeFile(outputList, "output.txt" )
    else:
        writeFile(outputList, fileNameOut)

main()