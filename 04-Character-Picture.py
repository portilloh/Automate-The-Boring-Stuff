grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

#We want to print this grid as if it flipped 90 degrees to the right.
#First iterate in each column. There are six columns, so once for each.
for y in range(len(grid[0])):
	#And in each row. There are 9 rows, so once for each.
	for x in range(len(grid)):
		print(grid[x][y],end='')
	print()

