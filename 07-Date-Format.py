"""
Write a regular expression that can detect dates in the DD/MM/YYYY format. 
Assume that the days range from 01 to 31, the months range from 01 to 12, and the years range from 1000 to 2999. 
Note that if the day or month is a single digit, it’ll have a leading zero.

The regular expression doesn’t have to detect correct days for each month or for leap years; 
it will accept nonexistent dates like 31/02/2020 or 31/04/2021.


Then store these strings into variables named month, day, and year, and write additional code that can detect if it is a valid date. 
	April, June, September, and November have 30 days, February has 28 days, 
	and the rest of the months have 31 days. 
	February has 29 days in leap years. 
	Leap years are every year evenly divisible by 4, except for years evenly divisible by 100, unless the year is also evenly divisible by 400. 
Note how this calculation makes it impossible to make a reasonably sized regular expression that can detect a valid date.

"""

#! python3

# date_format.py

# Start with the regular expression

import re, sys


DateRegEx = re.compile(r'''
	([0-2]\d|3[01]) 	# This is the day. Starts with either 0,1,or 2 and is followed by any digit. or starts with 3 and is followed by 0 or 1
	/					# Slash separatpr
	(0\d|1[012])		# Zero followed by any digit OR 1 followed by 0,1,or 2
	/					# Slash separatpr
	([12]\d\d\d)		# Year, starts with 1 or 2 and then 3 digits
	''', re.VERBOSE)



while True:
	date_entered = input('Please enter a date in dd/mm/yyy format: ')

	mo = DateRegEx.search(date_entered)

	if mo != None: # If the date matches the regex (therefore the matched object is not None)
		
		# Store day, month, and year in variables that will check if the date is valid.

		day = int(mo.group(1))

		month = mo.group(2)

		year = int(mo.group(3))

		if month in ['04', '06','08','11']:
			if day > 30:
				print('This month cannot have more than 30 days.')
		elif month == '02':
			if day > 29: # If it has more than 29 days, it's wrong.
				print('February has too many days')
			if day == 29:
				if year % 4 != 0: # Not divisible by four means it's not a leap year
					print(str(year) + ' is not a leap year. February has too many days.')
				elif year % 100 ==0 and year % 400 != 0: # Divisible by four and 100 but not by 400
					print(str(year) + ' is not a leap year. February has too many days.')
				else:
					print('Your date is valid')
		else: # If it's dibisible by four, 100, and 400, it's a leap year, in which case 29 is a good number of days.
			print('Your date is valid')
	else:
		print('This is not a valid format.')

	while True:
		run_again = str(input('Try again? (enter \'y\' for yes) \n' ))
		if run_again == 'y':
			break
		print('Program will exit now.')
		break
	if run_again == 'y':
		continue
	else:
		break
