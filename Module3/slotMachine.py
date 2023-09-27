# Slot Machine

# A player can insert any number of tokens into the machine.   Once the there are tokens in the machine,  the player can make a bet. The player can bet 1, 2, or 3 tokens.  Once they press Enter, three random numbers appear representing the slots on the slot machine with a range of 5 numbers. The player wins by getting all of the same random number.  If they win, they win tokens and that is added to are added to their amount. If the player loses, they lose the amount that they bet.

# The algorithm for winning tokens is as follows: The number they rolled to the power of the number they bet.
# So if they rolled all 2's and they bet 3 tokens, it would be 2 to the power of 3: or 8 tokens.
import random
import math

isActive = True
print("Murph E Cheese Slot Machine")
tokens = int(input("Enter the starting number of tokens you wish to use: "))

while isActive:
  bet = int(input("How much do you wish to bet? (Enter a number from 1 to 3, 4 to cash out): "))

  if bet == 1 or bet == 2 or bet == 3:
    num1 = random.randrange(1, 6)
    num2 = random.randrange(1, 6)
    num3 = random.randrange(1, 6)
    # num1 = 5
    # num2 = 5
    # num3 = 5
    print(num1, num2, num3)
    if num1 == num2 and num2 == num3:
      win = int(math.pow(num1, bet))
      tokens += win
      print(f"You win {win} tokens")
    else:
      tokens -= bet
      print(f"You lose {bet} tokens")
    print("Tokens:", tokens)

  if bet == 4:
    print(f"You receive {tokens} tokens\nThanks for playing!")
    isActive = False
