# readFile and replace character in line
# output = open('\tmp\abc', w)
# input = open('data',r)

# s = input.readline()
# L = input.readlines(s)
# output.write("string")

output = open('test2.txt', 'w')
with open('test1.txt', 'r') as fileToBeRead:
    print('read file test1.txt')
    for line in fileToBeRead:
        var1 = line.replace('line', 'sandeep')
        output.write(var1)
output.close()

print('Closed file test2.txt')
with open('test2.txt', 'r') as file2ToBeRead:
    print('reading file test2.txt')
    for line in file2ToBeRead:
        print(line)