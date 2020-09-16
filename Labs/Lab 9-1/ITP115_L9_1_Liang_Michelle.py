# Michelle Liang, liangmic@usc.edu
# ITP 115, Spring 2020
# Lab 9-1

import random
def coin():
    flip = random.randrange(2)
    if flip == 0:
        return "head"
    if flip == 1:
        return "tails"
def experiment():
    count = 0
    heads = 0
    while heads < 2:
        count += 1
        if coin() == "head":
            heads +=1
        else:
            heads = 0
    return count
def main():
    counter = 0
    total = 0
    runs = 10
    while counter < runs:
        counter+=1
        result = experiment()
        total = total + result
    # average
    average = total/runs
    print("The average for 3 heads in a row is", average, "flips")

main()