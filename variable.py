"""
Developer : Mandela Thomas
Date : 2/23/2024
subject: Learning Variable in Python
-------------------------------------
What is a variable
In Python, a varibale is a store container. One that store the value in memory.

"""


#Declaring variable
name = ""

#assigning variable
stock_exhange_name = "New York Stock Exchange"

#multiple variables and newline
name, major, school = "Mandela Thomas", "PHD in healthcare Management & Economics ", "Wharton University of Pennsylvania"
print(f"{name} is majoring in {major} \n at the {school} located Pennsylvania")

#reassigning a variable
former_name = "mandela philip Thomas"
current_name = "Philip mandela Thomas"
print(current_name)


#using global variable in a function
global weekly_hour_work

weekly_hour_work = int(input("Enter Week Work Hours : "))
def salary(hourly_rate, tax):
    paid_tax = tax * 1/100
    before_tax = weekly_hour_work * hourly_rate
    net_paid = before_tax - paid_tax 
    return net_paid
salary(40, 0.2)

    
    
    
    
    
