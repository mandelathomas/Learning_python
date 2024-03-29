
#using break and continue

"""
The break statement in python is
used to terminate the program out of the loop containing it whenever the condition is met.
"""

us_state = ['New York', 'Arizona', 'californa ', 'Utah']

for state in us_state:
  if state == 'new york':
    print('Yes, you are right ')

#Break, Continue, Pass
list1 = [4, 5, 6]
list2 = [10, 20, 30]

for i in list1:
    for j in list2:
        if j == 20:
            break #stops the execution here, ignores the print statement below and completely quits THIS "for" loop; however, it doesn't quit the outer "for" loop, too!
        print(i * j)
    print("Outside the nested loop")



list1 = [4, 5, 6]
list2 = [10, 20, 30]

for i in list1:
    for j in list2:
        if j == 20:
            continue #ignores the rest of the code below for the current iteration, then goes up to the top of the loop (inner "for") and starts the next iteration
        print(i * j)
    print("Outside the nested loop")



for i in range(10):
    pass #pass is the equivalent of "do nothing"; it is actually a placeholder for when you just want to write a piece of code that you will treat later
