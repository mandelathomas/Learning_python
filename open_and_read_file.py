"""
Python allow us to read from a file using (open() and read())
r	Default value. Opens a file for reading only. Raise an exception if the file does not exist.
r+	Opens a file for reading and writing. Raise an exception if the file does not exist.
w	Opens a file for writing only. Creates the file if it does not exist.
w+	Opens a file for reading and writing. Creates the file if it does not exist.
a	Opens a file for appending only. Creates the file if it does not exist.
a+	Opens a file for appending and reading. Creates the file if it does not exist.
x	Creates the specified file. Raise an exception if the file already exists.
x+	Creates the specified file and Opens the file in reading and writing mode. Raise an exception if the file already exists.
t	Default value. Opens a file in the text mode.
b	Opens a file in the binary mode.
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



#using the with-as solution, the files gets closed automatically, without needing the close() method
with open("python.txt", "w") as f: 
    f.write("Hello Python!\n")

#reading the file from the beginning 

file = open("reading.txt", "r")
file.read()
file.seek()


#open and read file 
print("Read whole file!")
file = open('json.txt', 'r')
print(file.read())

#Read a part of file
print("Read a part of the file!")
file = open('json.txt', 'r')
print(file.read(30))

#read file by line
print("Read file by line!")
file = open('json.txt', 'r')
print(file.readlines())

#Loop through the lines of the File

print("Loop over file!")
file = open('json.txt', 'r')
for txt in file:
  print(txt)

#close file
print("Read and close file!")
file = open('json.txt', 'r')
print(file.read())
file.close()

#Write to an Existing File
'''
"a" - append mode. to append to the end of the file.
"w" - write mode. to overwrite any existing content of the file.
'''
file = open('json.txt', 'a')
file.write("Python is a great language to learn from and be familar with if you wan to be a data scientist or engineer")
file.close()

#Create a New File
'''
"a" - append mode. Opens a file in append mode and creates the file if it does not exist.
"w" - write mode. Opens a file in write mode and creates the file if it does not exist.
"x" - create mode. Creates a file and raises exception if it already exists.
'''

file = open('python.txt', 'a')
file = open('python.txt', 'w')
file = open('python.txt', 'x')

#delete a file

import os
os.remove('python.txt')

#Check if File exist

if os.path.exists('python.txt'):
  os.remove('python.txt')
else:
  print("No such file with the name exist on this system. \n maybe, file was deleted or relcated")


#Delete Folder
import os
os.rmdir("myfoler")


