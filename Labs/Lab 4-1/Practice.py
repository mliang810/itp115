'''
num = int(input("give me a number: "))
#any number between 3-5 is winner (including 3 and 5)
if num >= 3 and num <= 5: # or write 3 < num < 5
    print("you win")
    print("good for you")

elif num<=2 and num >=5:
    print("so close")
else:
    print("you lose")
'''
'''
num = 10
while num <= 10 and num > 0:
    print(num)
    num = num - 1
print("Blast off")
'''
'''
numb = 0
for num in range(0,10):
    print(10 - num)

print("Blast off")
'''
'''
for num in range(10,0,-1):
    print(num, end = ", ")
'''
'''
for num in range(0, 26, 5):
    print(num, end=", ")
'''
'''
for letter in "Hello World":
   print("\"" + letter.upper() + "\", ", end = "")
'''
'''
    #or do this, but cant get rid of new line 
    strin = "\"" + letter + "\""
    strin = strin + ", "
    print(strin)
'''

num = len("Hello World")
print(num)

num = len(range(10))
print(num)

s = "spamalot"
if "spam" in s:
    print("yes")
else:
    print("no")

num = int(input("gimme a number "))
if num >= 3 and num <= 5:
    print("yay")
else:
    print("nope")
if num in range(3,6):
    print("yay")
else:
    print("nope")