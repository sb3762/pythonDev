#take a number input from the user and print that many elements of Fibonacci sequence

startingElement = input('whats your starting value of fibonacci :')
numberOfElements = input('How many elements of Fibonacci Sequence do you want to print :')

nOE = int(numberOfElements)
start = int(startingElement)
print ('number of elements needed to be printed : ', nOE)
print ('Starting value is  : ', start)

previousFib = start
prev = 0
print ('here -1 ')

print(start)  # print the first element outside the loop

for printNumber in range (start, nOE):
    #fib = prev + previousFib
    #print (fib)
    #prev = previousFib
    #previousFib = fib
    start = prev + previousFib
    print (start)
    prev = previousFib
    previousFib = start
print ('Completed')