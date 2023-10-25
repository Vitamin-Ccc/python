# Variable to store the decryption key
dKey = 0

while True:
  try:
    print("Please enter the key used to decrypt the file.")
    dKey = int(input())
    break
  except ValueError:
    print("Please enter a number.")
    print("Please try again.")

while True:
  try:
    print("Please enter the file you would like to decrypt.")
    fileName = input()

    # attempt to open the file to read from it
    f = open(fileName, 'r')

    # create a file to write the decrypted text to
    decryptedFile = open("decrypted.txt", "w")

    for line in f:
      for i in range(len(line)):
        # getting each character in the string
        letter = line[i]
        # getting the value of the letter
        chValue = ord(letter)
        # subtracting the decryption key
        chValue -= dKey
        # converting value back to letter
        letter = chr(chValue)
        # wrting to the file
        decryptedFile.write(letter)
    break

  except FileNotFoundError:
    print("File does not exist. Please enter the correct file name")
  except:
    print("Error Occurred")

print("File was decrypted to decrypted.txt")
# close the files
f.close()
decryptedFile.close()