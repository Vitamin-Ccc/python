# Write a program that checks the properness of a given variable name. More specifically, your program should specify whether a user-entered variable name is

# illegal (no spaces allowed, must begin with a letter)
# legal, but uses poor style (should only use letters or digits)
# good 

print("This program checks the properness of a proposed variable name.")
isActive = True

while isActive:
  name = input("Enter a variable name (q to quit): ")
  # quit if name = "q"
  if name == "q":
    isActive = False
  # if variable name contains space or if the first letter is a number
  elif name.find(" ") > 0 or name[0].isdigit(): 
    print("Illegal")
  # if all characters in the string are alphanumeric
  elif name.isalnum():
    print("Good!")
  else:
    print("Legal, but uses poor style.")