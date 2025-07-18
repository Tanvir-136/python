# Write a Python program that accepts an integer (n) 
# and computes the value of n+nn+nnn.

num = input("Enter and integer number: ")
result = int(num) + int(num * 2) + int(num * 3)
print("Result: ", result)


# output: 
# Enter and integer number: 5
# Result:  615