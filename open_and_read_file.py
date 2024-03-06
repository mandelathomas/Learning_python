"""
Python allow us to read from a file using (open() and read())
    r : read file
    a : appending file
    w: write to file
    x : exclusive creation
"""

#open the file to read from
file = open("reading.txt", "r")

#read from the file ton read from
print(file.read())

#just read from just a line
print(file.readline())

#seek to place the cursor at the middle of the text
file.seek(0)

#turning the text into list
print(file.readlines())

#using for loop with read line

for msg in file.readlines():
    if msg.startswith("C"):
        print(msg)

#using exclusion creation. Exclusion create a new file if it is does not exist

file = open('mytxt.txt', 'x')


