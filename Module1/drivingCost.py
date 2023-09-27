# It is a good idea to know your transportation costs! We are going to find out the costs to drive a car from Weber State to different areas in Utah . Write a program that asks for the input of 3 different areas in Utah and how many miles it takes to get from there to Weber State. Then ask for the car's gas mileage and the cost of gas as floating-point input, and outputs the gas cost for the 3 different areas you selected.

# With miles per gallon, trip distance and the price of gas, you can calculate the gas cost for the trip by dividing the distance of the route by your miles per gallon to discover how many gallons of gas you will need, then multiply the number of gallons by the price of gas.

# miles per gallon input
milesPerGallon = float(input("How many miles to the gallon does your car get? "))
# current cost of gas input
gasCost = float(input("What is the current cost of gas? "))
# first area input
firstArea = str(input("What is the first area you would like to calculate the cost to? "))
# distance to first area input
distanceFirstArea = float(input("How many miles is it to your first area from Weber State? "))
# driving cost calculation, area 1
result1 = round(distanceFirstArea/milesPerGallon * gasCost, 2)
# rounding for 2 digits after the decimal point, print driving cost
print("Driving cost for area 1 " + firstArea + ":", result1)

# second area input
secondArea = str(input("What is the second area you would like to calculate the cost to? "))
# distance to second area input
distanceSecondArea = float(input("How many miles is it to your second area from Weber State? "))
# driving cost calculation, area 2
result2 = round(distanceSecondArea/milesPerGallon * gasCost, 2)
# rounding for 2 digits after the decimal point, print driving cost
print("Driving cost for area 2 " + secondArea + ":", result2)

# third area input
thirdArea = str(input("What is the third area you would like to calculate the cost to? "))
# distance to third area input
distanceThirdArea = float(input("How many miles is it to your third area from Weber State? "))
# driving cost calculation, area 3
result3 = round(distanceThirdArea/milesPerGallon * gasCost, 2)
# rounding for 2 digits after the decimal point, print driving cost
print("Driving cost for area 3 " + thirdArea + ":", result3)