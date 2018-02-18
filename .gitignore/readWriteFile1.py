# readFile and replace character in line
# output = open('\tmp\abc', w)
# input = open('data',r)

# s = input.readline()
# L = input.readlines(s)
# output.write("string")

with open('test3.txt', 'r') as senderInfo:
    print('read the sender Info file')
    while(senderInfo):
        with open('message1.txt', 'r') as messageFile:
        print('read file message1.txt')
        inputMessage = messageFile.readline()
        print('printing content of line from message', inputMessage)
        var1 = inputMessage.replace('<customerName>', senderInfo)
        messageFile.close()
