# -*- coding: utf-8 -*-
"""excpetion.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1B_xJL7QJNDEypvmjjWH-az4I34QnMKDG
"""

"""
An exception is an object with a description of what when wrong and traceback where the problem occurs
"""

#try: It is used to test a block of statements for error.
#except: It has a block of statements which executes when error occurs and handles error.
#finally: It has a block of statements which executes regardless of try-except blocks result.


#accesing a file

name = input("Enter your full Name: ")
fname = name.split()[1]

try:
  file = open("anscombe.json")
  read_file = file.readline()
  print(read_file)

except:
  print(f"Sorry {fname}, There was an error accessing and reading the file!!")
  print("Please check your connection and try again!!")
finally:
  print('file has been cliosed!!')
  file.close()