from sys import argv
#filename = 'test1.txt' to be passed in the start
script, filename = argv

def print_all(f):
    print(f.read())


def print_line_by_line(f):
    with open(f, "r") as ins:
        for line in ins:
            print('line number: ', line)
    #close(f)
    #f.close()

print("we are reading {}:", format(filename))
target = open(filename, 'r')   # open file name as a writable file
print('printing all file contents in one go')
print_all(target)

target.close()

#target.seek(0)
print('Next printing all file contents Line by line')
print_line_by_line(filename)
#print(target)



