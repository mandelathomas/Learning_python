
"""
Using python dictionary
what is a dictionary?
A Dictionary is a type of data container in Python which is used to store multiple data in one variable.
"""

#creating an empty dictionary
dict1 = {} 

#Dictionary with multiple datatypes

arizona_Car_dealership = {

"maker" : "toyota ",
"mode" : "Camry",
"year" : 2024,
"engine_side" : 2.8
}

#Creating dictionary with constructor

richest_family = dict(family_name = "The Wilson Family", famil_size = 20, income_source = "oil and beauty")
print(richest_family)

#accesing dictionary elements

print(f"{richest_family['family_name']} are the richest South American family")
print(richest_family.get("family_name"))

#Modify values in Dictionary
richest_family['famil_size'] = 40
print(f"{richest_family['family_name']} have a size of {richest_family['famil_size']} members")

#Add elements in Dictionary
richest_family['family_wealth'] = '45.9 Billions'
print(f"{richest_family['family_name']} wealth is {richest_family['family_wealth']}")


#Loop over Dictionary's values
print(f"These are the full searched information on {richest_family['family_name']} :")

for info in richest_family.values():
  print(info)

#copying dictionary
new_family = richest_family.copy()
print(new_family )

#delecting in dictionary

#pop: deletes specified key and it's value of the dictionary
new_family.pop("family_name")
print(new_family)

#clear : deletes all key-value pairs of the dictionary.
new_family.clear()
print(new_family)

#Del : deletes a key-value pair of a dictionary. can be used to delete the dictionary itself.
del new_family

#--- Project
my_dict = {1: "Cisco", 2: "HP", 3: "Juniper", 4: "Arista", 5: "Avaya"}

max(my_dict.keys()) 
sorted(my_dict.values())[0]
len(my_dict) == 4


