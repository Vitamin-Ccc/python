# Write a program that simulates the rolling of two 6-sided dice.  Note that rolling two dice and adding them together is different than rolling a 11-sided dice. Use a Dictionary to keep track of the number of times that each total number is thrown. You may use the Key portion of the Dictionary as the sum of the two dice, and the Value portion to keep track of the number of rolls.  If the key does not exist, then set the value as 1.  If the key does exist, then add one to the value.

# Allow the user to choose how many times the “dice” will be thrown. Then, once the dice have been thrown the specified number of times, print out how many times each number was thrown.

# For 10 bonus points print a histogram (using the * character) that shows the total percentage each number was rolled. Each * will represent 1% of the total rolls.
import random

rollDict = { }
for i in range(1, 7):
  for j in range(1, 7):
    if i+j not in rollDict:
      rollDict[i+j] = 0
      
print("Welcome to the dice throwing simulator!")
times = int(input("How many dice rolls would you like to simulate? "))
print("DICE ROLLING SIMULATION RESULTS")
print("Total number of rolls =", times)

for i in range(times):
  sum = random.randrange(1, 7) + random.randrange(1,7)
  if sum in rollDict:
    rollDict[sum] += 1

for i in rollDict:
  print(str(i)+":", rollDict[i])

print("Thank you for using the dice throwing simulator. Goodbye!")