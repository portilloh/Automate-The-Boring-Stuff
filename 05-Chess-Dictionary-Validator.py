#We need a function that checks if the chess board is valid.
#This doesn't check if it's *possible* that the pieces are where they are (ie, doesn't check if the white bishop is in a white cell)/
#It checks to make sure the pieces are valid and placed within a valid chess board.

#Conditions for being a valid chess board:
# 	One black kind and one white king;
#	At most 16 pieces per player
#	At most 8 pawns each
#	Pieces have to be in columns a-h and rows 1-8
#	Pieces are either black or white and are only valid chess pieces

#This function needs to detect an invalid board and let the player know



def isValidChessBoard(chessboard):
	# Start with a True variable that will become false if the board is invalid
	valid = True

	#First we check to make sure there is exactly one king per color.
	wking =0
	bking=0
	
	#For every piece in the chessboard, if it's a white/black king add one to the respective counter.
	#The chessboard is a dictionary, in which the keys are the 'tiles' (e.g., 'a1', 'h8', etc) and the values are the pieces ('wking', 'bpawn')
	for piece in chessboard.values():
		if piece == 'wking':
			wking += 1
		if piece == 'bking':
			bking +=1

	if wking > 1:
		valid = False
		print("There is more than one white kind. This board is invalid")
	if wking == 0:
		print('There is no white king. This board is invalid')
		valid = False
	if bking > 1:
		valid = False
		print("There is more than one black king. This board is invalid")
	if bking == 0:
		valid = False
		print('There is no black king. This board is invalid')
	
	#Count the number of pieces per player
	wpieces=0
	bpieces=0
	for piece in chessboard.values():
		if piece.startswith('w'):
			wpieces += 1
		elif piece.startswith('b'):
			bpieces += 1
		# If the piece is not black or white the board is invalid
		else:
			valid = False
			print(piece + ' is neither black nor white. This board is invalid')

	if wpieces > 16:
		valid = False
		print('There are more than 16 white pieces. This board is invalid')
	if bpieces > 16:
		valid = False
		print('There are more than 16 black pieces. This board is invalid')


	#Count the number of pawns per player
	wpawns =0
	bpawns =0

	for piece in chessboard.values():
		if piece == 'wpawn':
			wpawns += 1
		if piece == 'bpawn':
			bpawns += 1
	#Check to see if there are more than 8 pawns of either color
	if wpawns > 8:
		valid = False
		print('There are more than 8 white pawns. This board is invalid')
	if bpawns > 8:
		valid = False
		print('There are more than 8 black pawns. This board is invalid')


	#Check that the pieces are within a1 and h8

	columns = ['1','2','3','4','5','6','7','8']
	rows = ['a','b','c','d','e','f','g','h']
	for tile in chessboard.keys():
		if tile[0] not in columns or tile[1] not in rows:
			valid = False
			print(tile + ' is not a valid tile. This board is invalid.')
		
	# Check that the pieces are valid	
	valid_pieces = ['king','queen','bishop','knight','rook','pawn']

	for piece in chessboard.values():
		if piece[1:] not in valid_pieces:
			valid = False
			print(piece + ' is not a valid chess piece')

	# Check if the board is valid after all the tests.
	if valid == True:
		print('This chessboard is valid')


		
board1 = {'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'} 

isValidChessBoard(board1)