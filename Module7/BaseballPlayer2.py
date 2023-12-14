class BaseballPlayer:

  def __init__(self):
    self.name = input("What is the player's name?")
    self.number = input("What is the player's number?")
    self.batting_avg = 0

  def calculate_batting_avg(self):
    hits = int(input("How many hits did the player get?"))
    at_bats = int(input("How many attempts to hit the ball did the player get?"))
    self.batting_avg = round(hits / at_bats, 3)
    return self.batting_avg

# main program
print("Welcome to the Player Tracker!")

player1 = BaseballPlayer()
player2 = BaseballPlayer()

print(player1.calculate_batting_avg())
print(player2.calculate_batting_avg())