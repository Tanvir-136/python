# Write a Python program to calculate the number of days between two dates.

from datetime import date

# Sample dates
date1 = date(2014, 7, 2)
date2 = date(2014, 7, 11)

# Calculate the difference
delta = date2 - date1

print(f"{delta.days} days")

# output
# 9 days