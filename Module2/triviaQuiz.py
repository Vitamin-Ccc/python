# To keep track of score
score = 0
print("Food Trivia")

# First question
iceCream = input("Which country invented ice cream?\n")
# converts the input to lowercase letters
if iceCream.lower() == "china":
  print("Yay!! You got it!")
  # adds one to the score
  score += 1
else:
  print("Oops, it was China")
# print current score
print("Score:", score, "out of 5")

# Second question
fries = input("Which country did the french fries originate from?\n")
if fries.lower() == "belgium":
  print("Yay!! You got it!")
  score += 1
else:
  print("Oops, it was Belgium")
# print current score
print("Score:", score, "out of 5")

# Third question
kfc = input("What was the first fast-food chain in China?\n")
# converts the input to lowercase letters, input can be "kfc" or "kentucky fried chicken"
if kfc.lower() == "kfc" or kfc.lower() == "kentucky fried chicken":
  print("Yay!! You got it!")
  score += 1
else:
  print("Oops, it was KFC")
print("Score:", score, "out of 5")

# Fourth question
coffeBeans = input("Which U.S. state is the only state to grow coffee beans?\n")
if coffeBeans.lower() == "hawaii":
  print("Yay!! You got it!")
  score += 1
else:
  print("Oops, it was Hawaii")
print("Score:", score, "out of 5")

# Final question
cake = input("Black Forest cake originated in which country?\n")
if cake.lower() == "germany":
  print("Yay!! You got it!")
  score += 1
else:
  print("Oops, it was Germany")
print("Score:", score, "out of 5")

# Calculate final percentage
percentage = int(score / 5 * 100)
print(f"Final Percentage: {percentage}%")