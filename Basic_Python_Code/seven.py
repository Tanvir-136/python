# Write a Python program that 
# accepts a filename from the user and prints the extension of the file. 

filename = input("Enter the filename: ")
extension = filename.split(".")[-1]

print("The extension of the file name is:", extension)

# output: 
# Enter the filename: abcd.py
# The extension of the file name is: py