# Dinosaur Park Party Calculator

# The Dinosaur Park is a super fun place for kids here in Ogden.  They allow parents to plan birthday parties for their kids.  Write a program to help parents calculate the cost of a party following the prices they set up for parties on their website.  

# Create a main menu of the party options, and a fourth option to quit the program.  After the user has selected their party option, the program will repeat the main menu to allow the user to calculate a different party or select the option to quit the program.
isActive = True
cost = 0

while isActive:
  print("Welcome to the Dinosaur Park Party Planner")
  print("Choose the type of party")
  print("1. Group Rate Admission Party")
  print("2. Bare Bones Package")
  print("3. Deluxe Party Package")
  print("4. Quit")
  choice = int(input("Enter choice: "))
  if choice == 1:
    groupAdults = int(input("Enter number of adults (13+ years old): "))
    groupChildren = int(input("Enter number of children (2-12 years old): "))
    if groupAdults > 0 or groupChildren > 0:
      cost += 5 * groupAdults
      cost += 3 * groupChildren
    print("Total cost will be: ", cost)
  if choice in range (2, 4):
    member = int(input("Are you a member? Press 1 for yes and 2 for no: "))
    if choice == 2 and member == 1:
      cost += 99
    elif choice == 2 and member == 2:
      cost += 119
    elif choice == 3 and member == 1:
      cost += 175
    elif choice == 3 and member == 2:
      cost += 199
    print("The base cost covers admission for up to 12 people. Enter in the amount of additional people:")
    adults = int(input("Additional adults: "))
    children = int(input("Additional children: "))
    if adults > 0 or children > 0:
      cost += 3 * adults
      cost += 3 * children
    print("Total cost will be: ", cost)
  if choice == 4:
    isActive = False
  cost = 0