import sys

blank_board = [ ["  1  ","  2  ","  3  "] ,
				["  4  ","  5  ","  6  "] ,
				["  7  ","  8  ","  9  "] ]
mapping = [ (1,0,0), (2,0,1), (3,0,2), (4,1,0), (5,1,1), (6,1,2), (7,2,0), (8,2,1), (9,2,2)]
row = [' ']*9
taken = []

def print_board() -> None:
	"""Helps us print the board with numbers in each box"""
	for i in range(3):
		row[i] = "|".join(blank_board[i])
	column = "-" * 15
	for i in range(3):
		print(row[i])
		if i==2:
			break
		print(column)
	return None
	
def map(str_1: str) -> None:
	"""Assigns X or O to the board"""
	if pos > 9:
		print("Invalid Input. \nQuitting")
		sys.exit()
	for i in range(9):
		if pos == mapping[i][0]:
			r = mapping[i][1]
			c = mapping[i][2]
			blank_board[r][c] = str_1

def win(str_2: str) -> None:
	"""Checks if anyone has won"""
	if (blank_board[0][0] == blank_board[0][1] == blank_board[0][2]) or (blank_board[1][0] == blank_board[1][1]  == blank_board[1][2]) or (blank_board[2][0] == blank_board[2][1] == blank_board[2][2]) or (blank_board[0][0] == blank_board[1][0] == blank_board[2][0]) or (blank_board[0][1] == blank_board[1][1] == blank_board[2][1]) or (blank_board[0][2] == blank_board[1][2] == blank_board[2][2]) or (blank_board[0][0] == blank_board[1][1] == blank_board[2][2]) or (blank_board[2][0] == blank_board[1][1] == blank_board[0][2]):
		print(str_2,"wins")
		sys.exit()

print_board()
while True:
	pos_inp = input("Where do you want X in?  ")
	if pos_inp in taken:
		print("Oops already taken.\nQuitting")
		sys.exit()
	taken.append(pos_inp)
	pos = int(pos_inp)
	map("  X  ")
	win("  X  ")
	
	if len(taken) == 9:
		print_board()
		print("It is a tie")
		sys.exit()
	
	print_board()
	pos_inp = input("Where do you want O in?  ")
	if pos_inp in taken:
		print("Oops already taken.\nQuitting")
		sys.exit()
	taken.append(pos_inp)
	pos = int(pos_inp)
	map("  O  ")
	print_board()
	win("  O  ")
	
	if len(taken) == 9:
		print("It is a tie")
		sys.exit()