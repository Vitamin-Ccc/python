print("Factors of a number")
num = int(input("Enter a number: "))
while num > 0:
  print("Factor of", num, end = ": ")
  for i in range(1, num+1):
    if num % i == 0:
      print(i, end= " ")
  
  num = int(input("Enter a number or -1 to quit "))