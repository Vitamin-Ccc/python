# Stuck in the Mud is a kid's dice game that reinforces adding and counting.  The rules are as follows.

# The first player rolls all five dice.  2s or 5s do not count as any points and are now stuck in the mud.  The rest of the dice are added up as the score for that throw.
# The player sets aside any 2s and 5s, and throws the remaining dice. Again, if any 2s or 5s are thrown, those dice are stuck in the mud.  The remaining dice are added to the score.
# Continue in this way until all the dice are “Stuck in the Mud.” After the score is totaled, play passes to the left.
# Write a program that will simulate one round of the Stuck in the Mud game.  Create an array for the dice and populate it with random numbers to simulate the dice.  Sum the values that are not equal to 2 and 5.  If the user chooses to roll again, roll only the values that are not stuck in the mud.
import random

print("Stuck in the Mud")

dices = []

