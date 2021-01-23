# We want to write a function that  takes any inventory and displays it like this:
# Inventory:
# 12 arrow
# 42 gold coin
# 1 rope
# 6 torch
# 1 dagger
# Total number of items: 62

#Initial Inventory
inv = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def displayInventory(inventory):
	print("Inventory: ")
	item_total=0
	for thing, numb in inventory.items():
		print(str(numb) + ' '+ thing)
		item_total += numb
	print('Total number of items: '+ str(item_total))


displayInventory(inv)

#Add an extra line
print()


#List to dictionary
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']


#Write a function that adds these to the inventory by updating the dictionary (inv)

def addToInventory(inventory,addedItems):
	print("Inventory Updated") #Add a line to let user know the inventory was updated.
	print()

	for thing in addedItems:
		inventory.setdefault(thing,0)
		inventory[thing]+=1
	return(inventory)



	# for thing in addedItems:
	# 	if thing in invent:
	# 		invent[thing]+=1
	# 	else: 
	# 		invent[thing] =1
	# return(invent)

#Update the inventory with the loot from the dragon
inv = addToInventory(inv,dragonLoot)

displayInventory(inv)