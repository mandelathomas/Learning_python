"""
Using condition in python
In Python, conditions are used to control the flow of your program based on whether certain statements are true or false.
They are crucial for making decisions within your code and creating more complex logic.

If / Elif / Else conditionals - executing code based on one or more conditions being evaluated as
True or False; the "elif" and "else" clauses are optional
"""

ans1 = "AMERICAN"
ans2 = "US CITIZEN"

name = str(input("Enter Full Name: "))
lname = name.split()[1]

question = str(input("Who is eligible to voter in the USA: "))

#Using the control flow
if question.upper() == ans1 or question.upper() == ans2:
  print(f"Your answer is correct {lname.capitalize()}!!")
else:
  print(f"Sorry {lname.capitalize()} your entry is wrong!!")
  print('Please try again')
