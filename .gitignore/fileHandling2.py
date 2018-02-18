from sys import argv
#filename = 'test1.txt'
script, filename = argv
print("we are erasing {}:", format(filename))
print("to cancel, hit CTRL-C")
print("to Continue, hit RETURN")

input("?")
print("opening file....")

target = open(filename, 'w')   # open file name as a writable file
target.truncate()

print("Now add something to the file")

newLine1  = input('enter your line that needs to be inserted into the file')
newLine2  = input('Enter Second line that needs to be inserted into the file')

target.write(newLine1)
target.write("\n")
target.write(newLine2)
target.close()

print(target)
