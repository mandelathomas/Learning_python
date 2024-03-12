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

#file = open('mytxt.txt', 'x')

#writing to the file

file = open('mytxts.txt', 'w')
file.write("you are a programmer, not a developer!! Please learn other languages to be more usable. Thanks")
file.close()

#write to line
file = open('mytxts.txt', 'w')
file.writelines("What is the differences between python and R. ")
file.close()


#write to line
file = open('mytxts.txt', 'a')
file.write("I am a man of my words. ")
file.close()

#writing and reading from the file
file = open("mytxts.txt", "r")
file.read()


with open('mytxts.txt', 'w') as mf:
    mf.closed
