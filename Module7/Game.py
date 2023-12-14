# Your part will be to write a separate class named RockPaperScissors that will interface with the main program.  Your class will contain three methods:

# getUserChoice:  Has the user choose Rock, Paper, or Scissors.  After checking to make sure the input is valid, the method will return a String containing the user choice.

# getCPUChoice:  Randomly generates a choice of Rock, Paper, or Scissors for the computer.  Returns a String containing the computer choice.

# pickWinner:  Is passed in two Strings that contain the user choice and the computer choice.  Compares the two choices and selects a winner.  Returns an int that indicates who the winner was:

# 0 = Tie
# 1 = User
# 2 = Computer
# Your class should interact with my class to make the game function correctly.
import random

class RockPaperScissors:
    def __init__(self):
        self.userChoice = ""
        self.cpuChoice = ""
        
    def getUserChoice(self):
        while True:
            choices = ["Rock", "Paper", "Scissors"]
            self.userChoice = input("Rock, Paper, or Scissors? ")
            try:
                if self.userChoice not in choices:
                    raise ValueError(f"Sorry, {self.userChoice} is not a valid entry.")
            except ValueError as err:
                print(err)
                continue
            break
        return self.userChoice
        

    def getCPUChoice(self):
        choices = ["Rock", "Paper", "Scissors"]
        self.cpuChoice = random.choice(choices)
        return self.cpuChoice
    
    def pickWinner(self, userChoice, cpuChoice):
        if userChoice == cpuChoice:
            return 0
        elif userChoice == "Paper":
            if cpuChoice == "Rock":
                return 1
            else:
                return 2
        elif userChoice == "Rock":
            if cpuChoice == "Scissors":
                return 1
            else:
                return 2
        elif userChoice == "Scissors":
            if cpuChoice == "Paper":
                return 1
            else:
                return 2
            


#Main Program
rps = RockPaperScissors ()  #***YOUR CLASS

print("Welcome to Rock, Paper, Scissors!")

hasError = False
numUserWins = 0
numCPUWins = 0

while True:
    try:
        
        #Reset error checker
        hasError = False
        
        #Get odd number of games
        numGames = int(input("How many rounds would you like to play? "))
        
        while numGames % 2 == 0: #Even number
        
            print("Sorry, number of games must be odd.  Please try again:")
            numGames = int(input("How many rounds would you like to play?"))
        
        break
        
    except ValueError as err:
        
        hasError = True
        
        print("Invalid input.  Please enter a number.")
        
		
#Play the game for the number of rounds the user entered allowing for ties with the count variable
count = 0
while count < numGames:

    #Get the user and computer choices
    userChoice = rps.getUserChoice()  #***YOUR METHOD
    cpuChoice = rps.getCPUChoice()   #***YOUR METHOD
    
    print("Computer chooses " + cpuChoice)
    
    #Pick winner
    winner = rps.pickWinner(userChoice, cpuChoice)  #***YOUR METHOD
    
    if winner == 0:
        print("It's a tie!  Play again.")
    elif winner == 1:
        print("User wins!")
        numUserWins+=1
        count += 1
    elif winner == 2:
        print("Computer wins!")
        numCPUWins+=1
        count += 1
    else:
        print("Error in picking winner!")

#Print results
print("\n\nUser wins: ", numUserWins)
print("Computer wins: ", numCPUWins)

if numUserWins > numCPUWins:

    print("The user won!")

if numCPUWins > numUserWins:

    print("The computer won!")


#Close game
print("\nThank you for playing!")
