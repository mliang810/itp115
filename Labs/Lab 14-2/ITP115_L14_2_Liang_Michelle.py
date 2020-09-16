# Michelle Liang, liangmic@usc.edu
# ITP 115, Spring 2020
# Lab 14-2

def readfile(fileName):
    fileIn = open(fileName, "r")
    count = 0
    dictionary = {}
    for line in fileIn:
        if line.strip() != "":
            count +=1
            temp = line.strip()
            words = temp.split(" ")
            for word in words:
                word = word.strip(",.!:?;")
                word = word.lower().capitalize()
                if word in dictionary:
                        dictionary[word].append(count)
                else:
                    dictionary[word] = [count]
    return dictionary

def sortKeys(dictionary):
    sortedKeyList = list(dictionary.keys())  # not sorted yet, just a list of the keys
    sortedKeyList.sort()
    return sortedKeyList

def main():
    file = "story.txt"
    dictionary = readfile(file)
    storyKeys = sortKeys(dictionary)
    print("Here is the concordance for the file " + "'" + file + "'")
    for key in storyKeys:
        print(key + ": ", dictionary[key])

main()
