#all About Python Math
"""
Learning Python math
"""

#Numbers
num1 = 10
num2 = 2.5

type(num1) #checking the type of this variable; integer
type(num2) #checking the type of this variable; float

#Numbers - math operations
a = 1 + 2 #addition

b = 2 - 1 #subtraction

c = 4 / 2 #division

d = 4 * 2 #multiplication

e = 4 ** 2 #raising to a power

f = 5 % 2 #modulo (this means finding out the remainder after division of one number by another)

#Numbers - float division vs. integer division (special case)
g = 3 / 2 #float division; result is 1 in Python 2 and 1.5 in Python 3

h= 3 // 2 #integer division; result is 1 in Python 2 and Python 3

#Numbers - order of evaluation in math operations
#Highest priority: raising to a power; Medium priority: division, multiplication and modulo; Low priority: addition and subtraction
i = 100 - 5 ** 2 / 5 * 2 #1st: 5 ** 2, second: / then *, third - ; result is 90.0

#Numbers - conversion between numeric types
int(1.5) #result is 1

float(2) #result is 2.0

#Numbers - useful functions
abs(5) #the distance between the number in between parantheses and 0

abs(-5) #returns the same result as abs(5)

max(1, 2) #returns the largest number

min(1, 2) #returns the smallest number

pow(3, 2) #another way of raising to a power
