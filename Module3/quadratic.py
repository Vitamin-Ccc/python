import math

print("Quadratic Formula")
a = float(input("Enter the value for a: "))
b = float(input("Enter the value for b: "))
c = float(input("Enter the value for c: "))

x1 = (-b + math.sqrt(math.pow(b, 2) - 4 * a * c)) / (2 * a)
x2 = (-b - math.sqrt(math.pow(b, 2) - 4 * a * c)) / (2 * a)

print("The solutions are:", x1, x2)