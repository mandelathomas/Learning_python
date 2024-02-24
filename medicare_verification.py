
"""
Building a usa medicare qualification system using Control flow
"""

#Developed: Feb 12, 2024
#Developer name : Mandela Thomas
#Project name: USA Medicare qualification system

# incomes and age Varification
medicare_age = 60
Medicare_individual_qualified_income =1235.00
Medicare__married_qualified_income = 1663.00

#user verification input
user_fullname = str(input("Enter Your Name: "))
age = int(input("Enter Age: "))

#separating the full name and only take the first name
last_name = user_fullname.split()[-1]

#user income verification
user_monthly_Household_income = float (input("Enter Household Income $"))

#check whether user meets the qualified income
if  user_monthly_Household_income  <= Medicare_individual_qualified_income  or age > 65:
  print(f"Congratulations {last_name.capitalize()}, you are qualified for Medicare!")
  
elif user_monthly_Household_income  > Medicare_individual_qualified_income :
  print(f"Sorry {last_name.capitalize()}, your monthly household income of {user_monthly_Household_income} is too high!")
  
else:
  print(f"Sorry {last_name.capitalize()}, You might find cheaper healthcare plan on healthcare.gov!")
