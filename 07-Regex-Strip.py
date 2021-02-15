#! pyton 3

# regex_strip.py

"""
This program takes a string and does what strip() does.
We use the first argument as the string to be passed and the second argument as the characters to be removed.
If the second argument is left empty, whitespace characters are removed from the beginning and end of the string.
"""

import re

def strip_2(string1,optional=''):
	if optional == '':
		funct_regex = re.compile(r'^(\s*)(\S*)(\s*$)') # Starts with 0 or more whitespace characters, 
													  #	is followed by 0 or more non-whitespace characters,
													  # Ends with 0 or more whitespace charcaters.
		mo = funct_regex.search(string1)
		print(mo.group(2))
	else:
		funct_regex = re.compile(optional)
		for_print = funct_regex.sub('',string1)
		print(for_print)


while True:

	text = input('Enter the string you want parsed: ')
	optional = input('Enter the text you want replaced (leave blank/press enter if you want to replace whitespace): ')

	strip_2(text,optional)

	while True:
		run_again = str(input('Enter \'y\' to try again. Press any other key to exit \n' ))
		if run_again == 'y':
			break
		print('Program will exit now.')
		break
	if run_again == 'y':
		continue
	else:
		break

