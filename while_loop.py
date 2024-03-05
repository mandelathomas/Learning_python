"""
Using control flow in python
In Python, the while loop is a fundamental control flow structure in Python used to
repeatedly execute a block of code as long as a certain condition remains true.
"""


#----- project1 -----

msg = """
USA Department Of Transportation
Check your eligibility for a driver's license in the US?
"""
print(f"Attention!! Attention!!\n {msg}")


#using  loop to get the matched requirement
driver_ssn = input("Enter Full Social Security Number: ")
while len(driver_ssn) <9 or len(driver_ssn) >9:
  driver_ssn = input("Enter Full Social Security Number: ")
  print("Sorry, your entrance exceeded or is below the maximum ssn")
  print("Please enter the nine digits number correctly!")

print("Please answer the next question!!")


#user entry and accessing their last name
driver_name = str(input("Enter Full legal Name: "))
lname = driver_name.split()[1]

#user birth year entry and subtracting to get the age
driver_birth_year = int(input("Enter Your Birth Year: "))
driver_age = 2024 - driver_birth_year


#age eligibility check up
if driver_age >16:
  print(f"Congratulations {lname.capitalize()}, you are eligible to drive in the USA")
  print("you can now take your written permit test!!")

else:
  print(f"Sorry {lname.capitalize()} you are not eligible to drive in the USA!!")


# ------- Project 2 ----

msg2 = """
Welcome to the USA driving permit test!!
"""
print(msg2)

#user name entry
name = str(input("Enter your full Name: "))
last_name = name.split()[1]

#user age entry
mimnum_age = 16
question = input("Enter the minimum driving age in the usa (type q to quit) : ")

#uing loop
while not question == "q":
  print(f"Sorry {last_name}, you did not get it right")
  question = input("Enter the minimum driving age in the usa: ")
print("Hope you getv your guess another time, bye")
