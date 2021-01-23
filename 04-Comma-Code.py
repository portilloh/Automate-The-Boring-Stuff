#We want a function that takes a user-entered list and returns a string with all the items separated by a comma and a space, with and inserted before the last item.

#Define function
#We will use the join() function.
def makestring(list):
	print(", ".join(list[:-1]) + ", and " + list[-1])


# Turn the user input, turn it into a list.
user_list =(input("enter the items on the list, only separated by a comma: ")).split(',')

makestring(user_list)
