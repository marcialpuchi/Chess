import os
from chess_ui import ChessUI
from board import Board
from rules import Rules


chess_ui =  ChessUI()
board = Board()

os.system('clear')
chess_ui.draw(board.getSimpleMap())

while True:
	
	lastMove = board.turn.enemy.moves[-1]

	if lastMove is not None: print "Last move:" + lastMove 
	print board.turn

	move = raw_input().split('-')
	rules = Rules(board, move[0], move[1])

	if rules.validateMove():
		board.move(move[0],move[1])
		os.system('clear')
		chess_ui.draw(board.getSimpleMap())
		board.lastMove = ''.join(move)

		if board.turn == board.p1:
			board.turn = board.p2
		else:
			board.turn = board.p1


		# if board.isChecked(board.turn):
		# 	board.pieces[board.getKing(board.turn)].checked = True

		# 	if len(board.checkDefensePositions(board.turn)) == 0:
		# 		print board.turn + ": Check Mate!! you lost"
			

		# 	print board.turn + ": Your king is under attack!"
		
		# else:
		#	board.pieces[board.getKing(board.turn)].checked = False

			
