# count number of lines having a word "abcde" and create a file with sentences and words
# >>>python3 myscript.py file1.txt abcde

from sys import argv
#script, filename, wordPattern = argv

#print("we are looking for pattern ", wordPattern,"in the file with name of ", filename)

def break_words(sentence):
    words = sentence.split(' ')
    return words

def sort_words(words):
    return sorted(words)

def count_wordPattern(sentence):
    words = break_words(sentence)
    sortedWords = sort_words(words)

def comparePattern(words, wordPattern, patternCounter):
    #patternCounter = 0
    for oneWord in words:
        if oneWord == wordPattern:
            patternCounter = patternCounter+1
    return patternCounter

def linesFromFile(fileName):
    txt = open(fileName, 'r')
    sentences = txt.readlines()
    print('The file has the following lines >> ', sentences)
    return sentences

def linesFromFile_oneByOne(fileName, wordPattern):
    patternCounter = 0
    with open(fileName, 'r') as fileToBeRead:
        print('read file ', fileName)
        for line in fileToBeRead:
            words = line.split()
            print(words)
            patternCounter = comparePattern(words, wordPattern, patternCounter)
        print(line)
        print('>>>>>>>> ', patternCounter)

    return line



