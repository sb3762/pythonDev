#readFile1 = open("test1.txt", "r")
#readFile2 = open("test2.txt", "r")

listNumber1= []         # create an empty list for contents of file 1
listNumber2 = []        # create an empty list for contents of file 2
overlapElementsList = [] # creare an empty list for overlapping contents of both files

with open('test1.txt', 'r') as readFile1:
    line = readFile1.readline() # read lines of file
    while line:
        #print(line)
        line = line.strip()
        listNumber1.append(line)   # convert the content into integer and store in list
        line = readFile1.readline()     # read next line
    print (listNumber1)

with open('test2.txt', 'r') as readFile2:
    lineAgain = readFile2.readline() # read lines of file
    while lineAgain:
        #print(lineAgain)
        lineAgain = lineAgain.strip()
        listNumber2.append(lineAgain)   # convert the content into integer and store in list
        lineAgain = readFile2.readline()     # read next line
    print (listNumber2)

for element in listNumber1:
    if element in listNumber2:
        overlapElementsList.append(element)
print("the common elements in both lists are -- ", overlapElementsList)
