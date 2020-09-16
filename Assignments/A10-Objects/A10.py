# Michelle Liang, liangmic@usc.edu
# ITP 115, Spring 2020
# Assignment 10

# Description:
# Creating the Animal class that contains information about each animal in the daycare, which is
# read in from a csv file. User will be able to interact with the animal given menu options (eg feed, play, etc)

class Animal():
    # constructor
    def __init__(self, hunger, happiness, health, energy, age, name, species):
        self.hunger = hunger
        self.happiness = happiness
        self.health = health
        self.energy = energy
        self.age = age
        self.name = name
        self.species = species

    # methods
    def play(self):
        self.hunger += 5
        self.happiness += 10

        if self.hunger <= 0:
            self.hunger = 0
        if self.hunger >= 100:
            self.hunger = 100
        if self.happiness <= 0:
            self.happiness = 0
        if self.happiness >= 100:
            self.happiness = 100

    def feed(self):
        self.hunger -= 10

        if self.hunger <= 0:
            self.hunger = 0
        if self.hunger >= 100:
            self.hunger = 100

    def giveMedicine(self):
        self.happiness -= 20
        self.health += 20

        if self.health <= 0:
            self.health = 0
        if self.health >= 100:
            self.health = 100
        if self.health <= 0:
            self.health = 0
        if self.health >= 100:
            self.health = 100

    def sleep(self):
        if self.energy < 81:
            self.energy += 20
        else:
            self.energy = 100
        if self.age >= 0:
            self.age += 1

    def __str__(self):
        result = "Name: "+ self.name + " the "+ self.species
        result += "\nHealth: "+ str(self.health) + "\nHappiness: "+ str(self.happiness) + "\nHunger: "
        result += str(self.hunger) + "\nEnergy: "+ str(self.energy) + "\nAge: "
        result += str(self.age)+ "\n********************************\n"
        return result

def loadAnimals(fileName = "animals.csv"):
    fileIn = open(fileName, "r")
    animalObjectList = []
    for line in fileIn: # make list of lists (each sublist is the attributes of a given animal)
        line = line.strip()
        temp = line.split(',')
        #convert digits in each line (aka for each animal) to integers
        for num in range(0,7):
            if temp[num].isdigit():
                temp[num] = int(temp[num])

        # make the object
        objectAnimal = Animal(temp[0], temp[1], temp[2], temp[3], temp[4], temp[5], temp[6])
        # insert specific Animal object into the list
        animalObjectList.append(objectAnimal)
    fileIn.close()
    return animalObjectList

def displayMenu():
    print("\n1) Play\n2) Feed\n3) Give Medicine\n4) Sleep\n5) Print an Animal's stats\n6) View All Animals\n7) Exit\n")

def selectAnimal(animalObjectList):
    print("1)", animalObjectList[0].name, "the", animalObjectList[0].species)
    print("2)", animalObjectList[1].name, "the", animalObjectList[1].species)
    print("3)", animalObjectList[2].name, "the", animalObjectList[2].species)
    print("4)", animalObjectList[3].name, "the", animalObjectList[3].species)
    print("5)", animalObjectList[4].name, "the", animalObjectList[4].species)
    keepAsking = True
    while keepAsking:
        choice = input("Please make a selection by entering a number from the list: ")
        if choice.isdigit():
            choice = int(choice)
            if choice in range(0,6):
                keepAsking = False
            else:
                print("Invalid entry, please try again")
    return animalObjectList[choice-1] # -1 to match index value

def saveAnimal(fileName, animalList): # extra credit
    fileOut = open(fileName, "w")
    for num in range(0, len(animalList)):
        print(str(animalList[num].hunger) + "," + str(animalList[num].happiness) + "," + str(animalList[num].health)
              + "," + str(animalList[num].energy) + "," + str(animalList[num].age) + "," + animalList[num].name
              + "," + animalList[num].species,file=fileOut)
    fileOut.close()

def main():
    animalList = loadAnimals()
    print("Welcome to the Animal Daycare! Here is what we can do: ")
    keepGoing = True
    while keepGoing:
        displayMenu()
        choice = input("Please make a selection: ")
        if choice.isdigit():
            if int(choice) in range(1,8):
                if choice == '7':
                    print("Goodbye!")
                    saveAnimal("savefile.csv", animalList) # extra credit
                    keepGoing = False
                elif choice == '6':
                    for num in range(0, len(animalList)):
                        print(animalList[num])
                else:
                    animal = selectAnimal(animalList)
                    if choice == '1':
                        animal.play()
                        print("You played with", animal.name, "the", animal.species)
                    elif choice == '2':
                        animal.feed()
                        print("You fed", animal.name, "the", animal.species)
                    elif choice == '3':
                        animal.giveMedicine()
                        print("You gave medicine to", animal.name, "the", animal.species)
                    elif choice == '4':
                        animal.sleep()
                        print(animal.name, "the", animal.species, "took a nap!")
                    elif choice == '5':
                        print(animal)
            else:
                print("Invalid input, try again.")
        else:
            print("Invalid input, try again.")
main()






