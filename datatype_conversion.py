
"""
converting between datatypes in python
data type conversion is useful mostly when we want to make the value the other
"""

#string  to a float
income = "100.00"
print(float(income))

#integer to a string and float
age = 30
print(str(age))
print(float(age))

#assigning an integer to user input
voter_age = int(input("Enter your votor age: "))
print(voter_age)

#list to tuple

cars = ["Jeep", "Ford", "BMW"]
print(tuple(cars))

#tuple to list
car = ("Jeep", "Ford", "BMW")
print(list(car))

# list to set

mycar = ["Jeep", "Ford", "BMW"]
print(set(mycar))

