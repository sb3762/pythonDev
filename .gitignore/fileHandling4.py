# copying one file to another
from sys import argv
from os.path import exists

#filename = 'test1.txt'
script, from_file, to_file = argv

print(f"copying from {from_file} to {to_file}")
# we could do these two on one line... how??

in_file= open(from_file)
indata = in_file.read()

print(f"The input file is {len(indata)} bytes long")
print(f"Does the outfile exists? {exists(to_file)}")
print("Ready, hit RETURN to continue, CTRL-C to abort...")

input()

out_file = open(to_file, 'w')
print("Alright.. All done.")
in_file.close()
