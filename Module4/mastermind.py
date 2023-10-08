import random

print("Mastermind")
secret = [ ]
for i in range(4):
  secret.append(random.randrange(1, 5))

posCorrect = 0
guesses = 0
maxGuesses = 15

# Keep the game going till they win or lose
while posCorrect < 4 and guesses < maxGuesses:
  guessArrayString = input("Enter your guess of four numbers: "). split()
  guesses += 1
  guessArrayInt = [int(i) for i in guessArrayString]

  tempSecret = secret.copy()
  tempGuessInt = guessArrayInt.copy()
  posCorrect = 0

  for i in range(len(tempSecret)):
    if tempSecret[i] == tempGuessInt[i]:
      posCorrect += 1
      tempSecret[i] = -1
      tempGuessInt[i] = -1
  colorsCorrect = 0

  for i in range(len(tempSecret)):
    for j in range(len(tempGuessInt)):
      if i != j and tempSecret[i] == tempGuessInt[j] and tempSecret[i] != -1:
        colorsCorrect += 1
        tempSecret[i] = -1
        tempGuessInt[i] = -1
        break

  print("Positions Correct:", posCorrect)
  print("Colors Correct:", colorsCorrect)

  if posCorrect == 4:
    print("You Win")
  elif guesses == maxGuesses:
    print("You Lose")

print("Secret combo was", secret)