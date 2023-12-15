# The purpose of this project is to demonstrate what you have learned throughout the semester.  In this choice, you will create a Cootie Catcher program that allows the user to player with a cootie catcher.

# As you create your Cootie Catcher, you will do so using an Object Oriented style of programming.  Create a Cootie class that contains data for the messages and final choice.  The messages will use a list with 8 messages to represent the possible options on the cootie catcher. 

# You will also have a method to allow the user to makeChoice().  For simplicity you can combine all of this into makeChoice(). If you want to create separate methods in the class for each of these you can choose to do that too. They first choose a color.  The color selected will allow different numbers to display based upon the number of letters the color has.  For example.  Should they choose "blue" the cootie catcher would toggle back and forth between the numbers 1, 2, 5, 6 and 3, 4, 7, 8 as the choices.  Since it is even, it would end on 1, 2, 5, 6 and from their the user could make their second choice.  Had it been "red" with only three letters, the cootie catcher would have ended up with 3, 4, 7, 8 as the numbers for the second choice.

class cootieCatcher:
  def __init__(self):
    self.color = ""
    self.odd = [3, 4, 7, 8]
    self.even = [1, 2, 5, 6]
    
  def makeChoice(self):
    while True:
      self.color = input("Choose a color(red, yellow, green, blue): ")
      if self.color.lower() == "red" or self.color.lower() == "green":
        while True:
            try:
              choice = int(input("Choose a number(3, 4, 7, 8): "))
              if choice in self.odd:
                if int(choice) == 3:
                  print("Cootie says: Positively Not")
                elif int(choice) == 4:
                  print("Cootie says: Maybe")
                elif int(choice) == 7:
                  print("Cootie says: Yes")
                else:
                  print("Cootie says: No")
                break
              else:
                print("Sorry, that is not an option.")
            except ValueError:
              print("Sorry, that is not a number. Please enter your choice in numeric format.")
              continue

      elif self.color.lower() == "blue" or self.color.lower() == "yellow":
        while True:
            try:
              choice = int(input("Choose a number(1, 2, 5, 6): "))
              if choice in self.even:
                if int(choice) == 1:
                  print("Cootie says: Absolutely")
                elif int(choice) == 2:
                  print("Cootie says: Believe in Yourself")
                elif int(choice) == 5:
                  print("Cootie says: Just Give Up")
                else:
                  print("Cootie says: You can do it")
                break
              else:
                print("Sorry, that is not an option.")
            except ValueError:
              print("Sorry, that is not a number. Please enter your choice in numeric format.")
              continue
      else:
        print("Sorry that is not an option")
        continue

      break

class gameStarts:
  isActive = True
  print("Cootie Catcher")
  while isActive:
    question = input("Ask your Cootie Catcher a question: ")
    player = cootieCatcher()
    player.makeChoice()
    while True:
      again = input("Would you like to (p)lay again or (q)uit? ")
      if again.lower() == "p":
        break
      elif again.lower() == "q":
        isActive = False
      else:
        print("Invalid response")
        continue
      break