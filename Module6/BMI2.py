print("Welcome to the Weber State University HUman Performance Lab!\nPlease utilize the following calculator to find your ideal fat burning heart rate and BMI.")

ageRun = 0
heightRun = 0
weightRun = 0

while True:
  # get age
  try:
    if ageRun == 0:
      age = int(input("Enter age: "))
      if age <= 0:
        ageRun += 1
        raise TypeError("Invalid age. Must be greater than 0.")
      break
    elif ageRun > 0:
      age = int(input("Re-enter age: "))
      if age <= 0:
        raise TypeError("Invalid age. Must be greater than 0.")
      # break
    ageRun = 0
    if heightRun == 0:
      height = int(input("Enter height in inches: "))
      if height <= 0:
        heightRun += 1
        raise TypeError("Invalid inches value. Must be positive.")
      break
    elif heightRun > 0:
      height = int(input("Re-enter height in inches: "))
      if height <= 0:
        raise TypeError("Invalid inches value. Must be positive.")
      continue
      # break
  except ValueError:
    ageRun += 1
    print("Invalid age. Must be a number.")
  except TypeError as err:
    print(err)

  # get height
  # try:
  #   if heightRun == 0:
  #     height = int(input("Enter height in inches: "))
  #     if height <= 0:
  #       heightRun += 1
  #       raise TypeError("Invalid inches value. Must be positive.")
  #     break
  #   elif heightRun > 0:
  #     height = int(input("Re-enter height in inches: "))
  #     if height <= 0:
  #       raise TypeError("Invalid inches value. Must be positive.")
  #     break
  # except ValueError:
  #   print("Invalid inches value. Must be a number.")
  # except TypeError as err:
  #   print(err)

print("Age =", age)
# print("Height = " + str(height) + '"')
# print("Weight =",weight,"pounds")

# bpm = (220 - age) * .7
# bmi = 703 * weight / (pow(height, 2))
# print("Fat Burning Heart Rate =", int(round(bpm)), "bpm")
# print("Body Mass Index =", round(bmi,1))