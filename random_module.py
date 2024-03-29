import random

"""
The random function can be used to generate a random number for any purpose,
such as choosing a random item from a list or generating a random number for a game.
The range function is typically used to generate a sequence of numbers for a loop.
The random function generates a random number
 between 0 and 1, while the range function generates a sequence of numbers.

"""
#random Integer
print("Welcome to Mandela Guessing Game")

#assigning the player
name = str(input("Enter your Full Legal Name: "))
fname = name.split()[1]
machine_player = random.randint(1,50)
human_player = int(input("Enter your matched number: "))

if human_player == machine_player:
  print(f"Congulations {fname} , your entry {human_player} match to {machine_player}")
  print("You won the game!!")
else:
  print(f'Sorry {fname}, you loss the game to {human_player} instead of {machine_player}')
  print("try again")

#random float and rounding it to the 2 decimal
number = random.random()
print(round(number, 2))

#using range

for num in range(10):
  print(num)
