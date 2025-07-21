# Write a Python program that prints the calendar for a given month and year.

import calendar

year = int(input("Enter year: "))
month = int(input("Enter month: "))

print("\nCalendar:")
print(calendar.month(year, month))

# Output:
# Enter year: 2025
# Enter month: 7

# Calendar:
#      July 2025
# Mo Tu We Th Fr Sa Su
#     1  2  3  4  5  6
#  7  8  9 10 11 12 13
# 14 15 16 17 18 19 20
# 21 22 23 24 25 26 27
# 28 29 30 31