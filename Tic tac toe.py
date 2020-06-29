#global var


board= ["-","-","-",
        "-","-","-",
        "-","-","-"]

# game still going

game_still_going = True
#winner
winner=None
#turn
current_player = "X"
def Display_board():
	print(board[0]+" | "+board[1]+" | "+board[2])
	print("---------")
	print(board[3]+" | "+board[4]+" | "+board[5])
	print("---------")
	print(board[6]+" | "+board[7]+" | "+board[8])

def handle_turn(player):
	print(player+"'s turn.")
	pos=input("choose a position from 1 to 9: ")
	valid = False
	while not valid:
		while pos not in ["1","2","3","4","5","6","7","8","9"]:
			pos=input("choose a position from 1 to 9: ")

		pos=int(pos)-1

		if board[pos]=="-":
			valid=True
		else:
			print("you can't go there. go again.")

	board[pos]=player
	Display_board()


def play_game():
	#Display board
	Display_board()
	#while the game is still going
	while game_still_going:
		handle_turn(current_player)
        #check if the game is ended
		check_if_gameover()
        #flip to the other player
		flip_player()
	if winner=="X" or winner=="O":
		print(winner+" won.")
	elif winner==None:
		print("Tie.")
		

def check_rows():

	global game_still_going


	row_1=board[0]==board[1]==board[2] !="-"
	row_2=board[3]==board[4]==board[5] !="-"
	row_3=board[6]==board[7]==board[8] !="-"
	if row_1 or row_2 or row_3:
		game_still_going=False
	if row_1:
		return board[0]
	elif row_2:
		return board[3]
	elif row_3:
		return board[6]

	return
def check_columns():
	global game_still_going


	column_1=board[0]==board[3]==board[6] !="-"
	column_2=board[1]==board[4]==board[7] !="-"
	column_3=board[2]==board[5]==board[8] !="-"
	if column_1 or column_2 or column_3:
		game_still_going=False
	if column_1:
		return board[0]
	elif column_2:
		return board[1]
	elif column_3:
		return board[2]

	return
def check_diagnols():
	global game_still_going


	diagonal_1=board[0]==board[4]==board[8] !="-"
	diagonal_2=board[6]==board[4]==board[2] !="-"
	
	if diagonal_1 or diagonal_2:
		game_still_going=False
	if diagonal_1:
		return board[0]
	elif diagonal_2:
		return board[6]
	

	return


def check_if_gameover():
	check_for_winner()
	check_if_tie()

def check_for_winner():
    #check rows ,coll,diag
    global winner


    row_winner=check_rows()

    column_winner=check_columns()

    diagonal_winner=check_diagnols()

    if row_winner:
    	winner=row_winner
    elif column_winner:
    	winner=column_winner
    elif diagonal_winner:
    	winner=diagonal_winner
    else:
    	winner=None
    return

def check_if_tie():
	global game_still_going
	if "-" not in board:
		game_still_going=False

	return

def flip_player():
	global current_player

	if current_player=="X":
		current_player="O"
	elif current_player=="O":
		current_player="X"
	return

play_game()