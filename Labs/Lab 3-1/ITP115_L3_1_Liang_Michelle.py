# Michelle Liang, liangmic@usc.edu
# ITP 115, Spring 2020
# Lab 3-1


# Description: Printing a triangle made of "^"

# def main():
#     lines = 0
#     carrots = "^"
#     spaces = 18
#
# #while loop to print the triangle made of 10 rows
#     while lines < 10:
#         theSpaces = " " * spaces
#         print(theSpaces + carrots)
#         lines +=1
#         carrots = "^ " + carrots + " ^"  #update carrots to have 2 more carrots per row
#         spaces -= 2                      #remove two spaces per line
#
# main()


def main():
    lines = 0
    carrots = "^"
    spaces = 18
    for lines in range(0, 10):
        theSpaces = " " * spaces
        print(theSpaces + carrots)
        carrots = "^ " + carrots + " ^"  # update carrots to have 2 more carrots per row
        spaces -= 2  # remove two spaces per line

main()