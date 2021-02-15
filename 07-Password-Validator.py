""" Regular Expression to make sure a string is a strong password.
Strong passwords:
	Have at least 8 characters
	Contains Uppercase and Lowercase characters
	Has at least one digit.
We can use multiple Regexes to test

"""

#! python3

# passwordvalidator.py tests a string to see if it's a strong password.

"""
We will need:
	1) A regex that checks the length of the string (8+ characters)
	2) A regex that checks to see if the password contains uppercase letters
	3) A regex that checks to see if the password contains lowercase letters
	4) A regex that checks to see if the password contains at least one digit.

"""

import re

# Regex to validate lenght of password

pass_len_regex = re.compile(r'\w{8,}')


# Regex to validata that there is at least one uppercase character
pass_uppercase_regex = re.compile(r'[A-Z]+')


# Regex to validata there is at least one lowercase character
pass_lowercase_regex =  re.compile(r'[a-z]+')

#Regex to validate there is at least one digit
pass_digit_regex = re.compile(r'\d+')


while True:
	pass_entered = input('Please enter your password: ')

	mo_length = pass_len_regex.search(pass_entered)
	mo_uppercase = pass_uppercase_regex.search(pass_entered)
	mo_lowercase = pass_lowercase_regex.search(pass_entered)
	mo_digit = pass_digit_regex.search(pass_entered)
	error_count =0

	if mo_length == None:
		print('Your password does not have the right lenght. Please make sure it\'s at least 8 characters')
		error_count += 1
	if mo_lowercase == None:
		print('Your password does not have any lowercase letters.')
		error_count += 1
	if mo_uppercase == None:
		print('Your password does not have any uppercase letters.')
		error_count += 1
	if mo_digit == None:
		print('Your password does not have any digits.')
		error_count += 1
	if error_count == 0:
		print('Password is valid. Good job.')


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