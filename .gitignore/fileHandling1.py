from sys import argv
#filename = 'test1.txt'
script, filename = argv
txt = open(filename)
print(f"Here is your file {filename}:")
# use this format in python 2.x ...print("here is your file{}: ", format(filename))
print (txt.read())
print("Please type the filename again:")
file_again = input(">")
txt_again = open(file_again)
print(txt_again.read())
