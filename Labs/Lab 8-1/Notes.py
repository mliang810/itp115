"""
def inputNum():
    ageLocal = input("How old are you? (in integers please) ")
    while not ageLocal.isdigit():
        ageLocal = input("How old are you? (in integers please) ")
    return ageLocal # returns age to outside the function
def main():
    age = inputNum() # insert the local variable into a variable in main()
    print("You are " + age + " years old.")

main()
"""
"""
def display(msg): # declaring a variable to be used inside this function, an input for this function
    print(msg)
    # no return because you dont need the "answer", this is a void function
    
def main():
        myList = ["lemon", "banana", "cherry"]
        for fruit in myList:
            display(fruit)
main()
"""

def add2numbers(a, b):
    c = a + b
    print(c)

def main():
    add2numbers(4,5)
    add2numbers("beautiful", "cake") #in python, varialbes can be ANY type, dont need to declare first like in C
    add2numbers("beautiful", 9)  # BUT when adding them etc, they should be the same
main()