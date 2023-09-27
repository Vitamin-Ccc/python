# Tip Calculator
# Allow the user to enter the cost of the meal
# Allow the user to enter the service: Excellent, Good, Poor
#  Calculate total cost of the meal

print("Tip Calculator")
cost = float(input("Enter the cost of your meal: "))
service = input("How was the service? Excellent, Good, Poor: ")

percentage = .10

if service == "Excellent" or service == "excellent":
  percentage += .10
elif service == "Good" or service == "good":
  percentage += .05

tip = cost * percentage
cost += tip

print("Tip: ", round(tip, 2))
print("Cost:", round(cost,2))