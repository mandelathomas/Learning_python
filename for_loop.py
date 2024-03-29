
"""
The primary purpose of a for loop in Python is to iterate over a sequence of items,
which can be a list, tuple, string, dictionary, set, or even a custom iterator object.
 This means it repeatedly executes a block of code for each item in the sequence.

"""

#looping over a list
Ohio_Dealership = ['Toyota', 'Honda', 'BMW', 'Jeep', 'Kia', 'Accura', 'Ford', 'GMC']
model = ['Camry', 'Civics', 'bi200', 'Grand g', 'k300', 'A700', 'f1500', 'silvarado']

for cars in Ohio_Dealership:
  print(cars)

  #looping over string

  name = "Thomas"
for myname in name:
  print(myname)

  #looping over a set
  numbers = {100, 200, 300, 400, 500}
  for x in numbers:
    print(x)


  #looping over a dictionary'
  mycars = {
  'maker' : 'Toyota',
  'year': '2024',
  'Purchased': '28,0000',
  'color': 'white'
}

for new_car in mycars:
  print(new_car)
