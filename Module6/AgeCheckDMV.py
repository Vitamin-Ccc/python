print("Welcome to the DMV.")
print("Please use this program to determine if you can apply for a driver's license.")

while True:
  try:
    age = int(input("What is your age? "))

    # force a number greater than 0
    if age <= 0:
      raise TypeError("Enter a number greater than zero.")
    break
  except ValueError:
    print("Invalid input")
    print("Please enter your age in numeric format.")
  except TypeError as err:
    print(err)
  except:
    print("Invalid input")

if age < 15:
  print("You cannot apply.")
elif age == 15:
  print("You can apply for a permit and driver's education course.")
elif age >= 16:
  print("You can apply.")