# Write a Python program that accepts a sequence of 
# comma-separated numbers from the user 
# and generates a list and a tuple of those numbers. 

numbers = input("Enter comma-separated numbers: ")

# Generating list and tuple
num_list = numbers.split(",")
num_tuple = tuple(num_list)

print("List :", num_list)
print("Tuple :", num_tuple)


# output: 
# Enter comma-separated numbers: 2, 3 , 4, 5
# List : ['2', ' 3 ', ' 4', ' 5']
# Tuple : ('2', ' 3 ', ' 4', ' 5')