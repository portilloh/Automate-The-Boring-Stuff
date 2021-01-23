#We want to generate a collatz sequence from whichever integer the user inputs
#First, we Define the collatz function

def collatz(number):
	# Check to see if the number is 1. If it is, print "Complete!"
	if number == 1: 
		print('Complete!')
	# Check to see if the number is even. If it is, divide it by two.
	elif number % 2 == 0:
		print(number //2)
		collatz(number//2)
	# If the number is not 1 and not even, it's odd (and not one).
	#In that case, multiply by 3 and add 1
	else:
		print(3*number + 1)
		collatz(3*number + 1)


#We want this to be iterated.
#We use a while true loop to create an infinite loop (True is always True)

while True:
	user_input=(input('Enter a number: '))
	try:
		collatz(int(user_input))
	except ValueError:
		print("You must enter an integer")
		#We add a "continue" statement so that Python returns to the loop instead of breaking.
		continue

#This still doesn't handle errors if the user enters a negative value.