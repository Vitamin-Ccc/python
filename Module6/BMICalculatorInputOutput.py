# Write a program that calculates an adult's fat-burning heart rate and BMI. The fat-burning heart rate is calculated by subtracting the person's age from 220. The result of this is the maximum heart rate and for fat burning 70% of the maximum would be needed. For example if the age entered is 40 then the maximum heart rate is 180 and 70% of this 126 bpm. This would be the persons fat burning heart rate.

# Body mass index is a measure of whether someone’s weight is appropriate for their height. A body-mass-index value between 19 and 25 is considered to be in the normal range.

# Perform input validation using exception handling by making sure the user enters only numbers (no strings!) and that those numbers are positive.

print("Welcome to the Weber State University Human Performance Lab!\nPlease utilize the following calculator to find your ideal fat burning heart rate and BMI.\nThe program will also store this information in a file you choose so that it can be tracked over time.")
ageRun = 0
heightRun = 0
weightRun = 0

info = {"fbhr" : 0, }

while True:
  while True:
    try:
      # Prompt user to select one of the following
      print("Select:")
      print("1. Create a file\n2. Open a file to add results to\n3. Read results from file")
      choice = int(input())
      break
    except ValueError as err:
      print(err)

  if choice == 1:
    # Prompt user to enter a file name
    print("Enter the name of the file you would like to create:")
    fileName = input()
    # Create empty file
    bmiFile = open(fileName, 'x')

  elif choice == 2:
    try:
      print("Enter the name of the file you would like to add to:")
      fileName = input()
      # Create empty file
      bmiFile = open(fileName, 'a')
    except FileNotFoundError:
      print("File not found.")

  elif choice == 3:
    try:
      bmiFile = open(fileName, 'r')
      print(bmiFile.read())
    except FileNotFoundError:
      print("File not found, please create a file first.")
    break

  else:
    break

  while True:
    try:
      # get age
      if ageRun == 0:
        age = int(input("Enter age: "))
        if age <= 0:
          ageRun += 1
          raise TypeError("Invalid age. Must be positive.")
      elif ageRun > 0:
        age = int(input("Re-enter age: "))
        if age <= 0:
          raise TypeError("Invalid age. Must be positive.")
    except ValueError:
      ageRun += 1
      print("Invalid age. Must be a number.")
      continue
    except TypeError as tErr:
      print(tErr)
      continue
    break

  while True:
    # get height 
    try:
      if heightRun == 0:
        height = float(input("Enter height in inches: "))
        if height <= 0:
          heightRun += 1
          raise TypeError("Invalid inches value. Must be positive.")
      elif heightRun > 0:
        height = float(input("Re-enter height in inches: "))
        if height <= 0:
          raise TypeError("Invalid inches value. Must be positive.")
    except ValueError:
      heightRun += 1
      print("Invalid inches value. Must be a number.")
      continue
    except TypeError as tErr:
      print(tErr)
      continue
    break

  while True:
    # get weight
    try:
      if weightRun == 0:
        weight = float(input("Enter weight in pounds: "))
        if weight <= 0:
          weightRun += 1
          raise TypeError("Invalid pounds value. Must be positive.")
      elif weightRun > 0:
        weight = float(input("Re-enter weight in pounds: "))
        if weight <= 0:
          raise TypeError("Invalid pounds value. Must be positive.")
    except ValueError:
      weightRun += 1
      print("Invalid pounds value. Must be a number.")
      continue
    except TypeError as tErr:
      print(tErr)
      continue
    break

  print("\nAge =", age)
  print("Height = " + str(height) + '"')
  print("Weight =",weight,"pounds")

  bpm = int(round(220 - age) * .7)
  bmi = round(703 * weight / (pow(height, 2)), 1)

  try:
    bmiFile = open(fileName, 'a')
    # write to a file
    bmiFile.write(f"FBHR: {bpm}bpm - BMI {bmi}\n")
  except:
    print("Error writing to file")

  print(f"\nFat Burning Heart Rate = {bpm}bpm")
  print(f"Body Mass Index = {bmi}")
  print("\nResults added to file.\n")

bmiFile.close()