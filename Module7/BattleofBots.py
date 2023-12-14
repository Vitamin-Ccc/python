# Welcome to Weber's Battle of the Bots!

# Create a simple robot battle game between two robots. Both bots start out with 100 life points. Every time the bots battle, the strength is based off a random number.  You can decide how to set the algorithm for strength. The bot with the most strength wins and the other bot loses life points (once again, you can decide the algorithm for how much life points they lose).

# This will be an Object-Oriented Program so you will create a botPlayer class and instantiate two objects of that class for each robot.  Some instance attributes about the class include...

# life points
# strength
# generator for a random number
# init

# A default to set the life points and strength
# Behaviors could include...

# set Strength
# receive damage
# You will need to access...

# strength
# life points

import random

class botPlayer:
  def __init__(self):
    self.health = 100
    self.strength = 0
    self.turn = 0

  def setStrength(self):
    self.strength = random.randint(1, 26)

  def receiveDamage(self, damage):
    self.health -= damage

  def changeTurn(self):
    self.turn += 1

class botGame:
  bot1 = botPlayer()
  bot2 = botPlayer()

  while True:
    print(f"Bot1 Life Points: {bot1.health}")
    print(f"Bot2 Life Points: {bot2.health}")

    if bot1.turn % 2 == 0 :
      print("Bot1 Your Turn!")
    else:
      print("Bot2 Your Turn!")

    choice = input("Press h to hit, q to quit: ")

    if choice != "h":
      break

    bot1.setStrength()
    bot2.setStrength()

    print(f"Bot1 strength: {bot1.strength}, Bot2 strength: {bot2.strength}.")
    if bot1.strength > bot2.strength:
      damage = int(bot1.strength - bot2.strength)
      bot2.receiveDamage(damage)
      print(f"Bot2 has {damage} points of damage.")
    elif bot1.strength < bot2.strength:
      damage = int(bot2.strength - bot1.strength)
      bot1.receiveDamage(damage)
      print(f"Bot1 has {damage} points of damage.")
    else:
      print("It was a tie")

    bot1.changeTurn()

    if bot1.health <= 0 or bot2.health <= 0:
      break


  print("Nice battle!")
  if bot1.health > bot2.health:
    print("Bot1 wins this round!")
  elif bot1.health < bot2.health:
    print("Bot2 wins this round!")
  else:
    print("Tie!")
  print("Thanks for playing!")