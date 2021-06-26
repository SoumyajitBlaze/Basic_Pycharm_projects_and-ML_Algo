# Python program to display calendar of given month of the year

# import module
import calendar


# To ask month and year from the user
year= input("Enter year: ")
month = input("Enter month: ")

# display the calendar
print(calendar.month(year, month))