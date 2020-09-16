'''
wantCream = input("Do you want cream? (y/n) ")
while wantCream.lower() != "y" and wantCream.lower() != "n":  #lower converts the string into all lowercase
    print("Error, try again.")
    wantCream = input("Do you want cream? (y/n) ")

if wantCream.lower() == "y":
    print("Here's some cream.")
else:
    print("Ok, no cream")

'''

'''
numBottles = 99

while numBottles > 0:
    print(numBottles, " bottles of coffee on the wall") # or str(numBottles) + "string"
    print("Take one down and pass it around")
    numBottles -=1
    print(numBottles, " bottles of coffee on the wall\n")

print("We finished all the coffee on the wall!")
'''

'''
wantCream = input("Do you want cream? (y/n) ")
while cream != "y":
    cream = input("Want cream?")

done = False
while not done:
    cream = input("Want cream?")
    if cream == "y"
        done = True

print("you get cream")
'''
'''
####### do while loop, must run at least 1 time bc we set it to run false the first time around
cream = "bad input"
while cream.lower() != "y" and cream.lower() != "n":
    cream = input("Want cream? (y/n) ")
 
if cream.lower() == "y":
    print("You get cream")
else:
    print("OK, no cream")
'''