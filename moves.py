import itertools
import pieces

class Moves(object):

	"""
	The Class Moves is the one that controls all the moves on a board
	by checking what moves can a particular piece make taking into
	considerations the rest of the pieces on the board.

	The class Moves contains the following variables:
		- pieces: A dictionary that uses the position of a piece on the
				  board as the key to map the pieces.

				  This allows the class to validate all the moves based
				  on the rest of the pieces located on the board.
	"""
	def __init__(self):
		pass


	"""
	move(): Allows to move a piece on the board from its original position
			to a new location.

			It takes two arguments:
				- old_pos: Refers to the position of the piece that is
						   going to change positions.
				- new_pos: Is the target position that the piece will
						   end up on.
	"""
	def move(self, old_pos, new_pos):
		self.turn.moves.append(old_pos+new_pos)

		# Change the piece to its new position.
		self.turn.map[new_pos] = self.turn.map[old_pos]

		# Remove the old piece from the old location.
		del self.turn.map[old_pos]
		
		# Update the move counter for that particular piece.
		piece = self.turn.map[new_pos]
		piece.updateCount(1)

		

	"""
	tryMove(): Allows a move to be validated before actually moving the piece.
			   It takes into consideration that:
			   		- The pieces should exist.
			   		- The piece belong to the player in turn.
			   		- The target position is in the list of available positions
			   		  to move for that particular piece.

			   	It takes two arguments:
				- old_pos: Refers to the position of the piece that is
						   going to change positions.
				- new_pos: Is the target position that the piece will
						   end up on.
	"""
	def tryMove(self, old_pos, new_pos):

		# The piece should exist
		piece = self.turn.getPiece(old_pos)
		if piece is False:
			print 'Piece not found @ ' + old_pos + ' or doesn\'t belong to you'
			return False

		king = self.turn.getKing()[1]
		
		if king.checked:
			av = self.checkDefensePositions(piece.color)
			if (old_pos, new_pos) not in av:
				print "Invalid Move: You have to defend the king, try another move."
				return False
		else:

			# The target position should exist in the list of allowed moves.
			av = self.getAvailableMoves(old_pos)
			if new_pos not in av:
				print 'Invalid Move'

				if len(av) != 0:
					print 'Available moves:', av
				else:
					print 'No available moves for ' + old_pos
				return False

		# If all the conditions mentioned above are met, the piece can be moved.
		self.move(old_pos, new_pos)
		return True

	def attackPositions(self, player):
		attack_pos = {}

		# Gather all attack moves that the player can make.
		for pos, piece in player.map.iteritems():
			attack_pos[pos] = self.getAvailableMoves(pos)

		return attack_pos


	"""
	isChecked(): Checks if a King piece is still in status check. If a King is checked,
				 the moves should be restricted to those that change this status.

				 It takes one argument:
				 	- color: Referes to the king piece owned by that player.
	"""
	def isChecked(self, color):

			opponent = 'white' if color is 'black' else 'black'
			attacks = self.attackPositions(opponent)
			attack_pos = set()
			king_pos = self.getKing(color)

			for piece, pos in attacks.iteritems():
				attack_pos |= pos

			# If the position of the king is in the list of attack positions
			# The King is in status check.
			return True if king_pos in attack_pos else False


	"""
	getAvailableMoves(): It gathers all the available moves a particular type of
						 piece can make depending on its position on the board
						 and all the other pieces on the board.

						 It takes one argument:
						 	- piece_pos: Is the location of the piece for which we
						 				 we need to compute the available moving
						 				 positions.
	"""

	def checkDefensePositions(self, color):
		opponent = 'white' if color is 'black' else 'black'
		team = self.getPlayerMap(color)
		attack_pieces = self.attackPositions(opponent)
		defend_pieces = self.attackPositions(color)
		king_pos = self.getKing(color)

		threats = [pos for pos, attacks in attack_pieces.iteritems() if king_pos in attacks]
		print "Attacking pieces: " + str(threats)

		av = set()
		
		# Attack
		for threat in threats:
			for pos, attacks in defend_pieces.iteritems():
				if threat in attacks:
					av.add((pos, threat))

		
		# Run away
		#defend_pieces[king_pos]
		run_away = self.getAvailableMoves(king_pos)
		attack_positions = set()

		# Get the set of attack positions
		for piece, attack in attack_pieces.iteritems():
			attack_positions |= attack

		# Check for a run-away position
		for move in run_away:
			if move not in attack_positions:
				av.add((king_pos, move))

		# Block attack

		# Get the set of attack positions
		# for piece, defend in defend_pieces.iteritems():
		# 	for threat in threats:

		# 		block_path = self.getPathTo(threat, king_pos)

		# 		for d in defend:
		# 			if d in block_path:
		# 				av.add((piece, threat))

		return av

	def getPathTo(self, origin, target):

		origin = list(origin)
		target = list(target)

		# Same column
		if origin[0] == target[0]:
			print "Same column"
			return self.getFwMoves(params)

		# Same row
		elif origin[1] == target[1]:
			print "same row"
			return self.getFwMoves(params)

		# up + right
		elif origin[1] == target[1]:
			print "diagonal up+right"
			return self.getFwMoves(params)

		# up + left
		elif origin[1] == target[1]:
			print "diagonal up+left"
			return self.getFwMoves(params)

		# down + right
		elif origin[1] == target[1]:
			print "diagonal down+right"
			return self.getFwMoves(params)

		# down + left
		elif origin[1] == target[1]:
			print "diagonal down+left"
			return self.getFwMoves(params)

		return []




	def getAvailableMoves(self, piece_pos):
		moves = []

		# Get the piece at the given position
		piece = self.getFullMap()[piece_pos]

		# Gather all the necessary parameters to compute the positions.
		params = {
			'piece': piece,
			'piece_pos': piece_pos,
			'col': list(piece_pos)[0],
			'row': int(list(piece_pos)[1]),
			'dir': self.turn.dir,
			'reach': piece.reach,
			'v_boundary': [9,0],
			'h_boundary': [self.addToChar('a', -1), self.addToChar('h', 1)],
			'color': self.turn.color
		}

		# Get all the possible directions in which a particular type of
		# piece can move.
		for direction in piece.getDirections():

			# Forward
			if direction == 'fw':
				moves += self.getFwMoves(params)

			# Backwards
			if direction == 'bw':
				moves += self.getBwMoves(params)
			
			# Left
			if direction == 'le':
				moves += self.getLeMoves(params)
			
			# Right
			if direction == 'ri':
				moves += self.getRiMoves(params)
			
			# Forward Diagonal /
			if direction == 'ld':
				moves += self.getFwDMoves(params)
			
			# Backward Diagonal \
			if direction == 'rd':
				moves += self.getBwDMoves(params)

			# Circle
			if direction == 'cr':
				moves += self.getCrMoves(params)

		return set(moves)


	"""
	addToChar(): A utility that allows us to add or subtract a number
				 to a char.

				 It will return the char that represent the sum of the
				 parameter.

				 It takes 2 parameters:
				 	- c: original charachter.
				 	- v: value to add/subtract from c.
	"""
	def addToChar(self, c, v):
  		return chr(ord(c)+v)


  	"""
	addToChar(): A utility that allows us to calculate a new position
				 on the board by adding or subtract a number to the
				 row and the column of the original position.
				 
				 It takes 3 parameters:
				 	- pos: Original position of a piece on the board.
				 	- sum_col: number to add/substract to the columns.
				 	- sum_row: number to add/substract to the rows.
	"""
  	def addToPos(self, pos, sum_col, sum_row):
  		col = list(pos)[0]
  		row = int(list(pos)[1])

  		return chr(ord(col)+sum_col) + str(row + sum_row)


  	"""
  	getFwMoves(): Calculates the forward moves that a given piece can make.
  	"""
	def getFwMoves(self, params):
		moves = []

		# Setup the reach of this particular piece.
		tmp_reach = params['reach']

		# Calculate the first temporary row, taking into consideration the
		# direction in which the piece moves.
		row = params['row'] + params['dir']

		# Get all the positions of the pieces that belong to the player that
		# owns the piece.
		team = self.turn.map.keys()

		# Keep moving until reaching the boundaries of the board or reach limit
		# of the moves this piece can do in one turn.
		while row not in params['v_boundary'] and tmp_reach != 0:

			# Create the position
			tmp_move = params['col']+str(row)

			# Stop if there is someone of the same team
			if tmp_move in team:
				break

			# Otherwise, you can move to this position
			moves.append(tmp_move)

			# If the position is occupied by enemy piece, stop.
			if tmp_move in self.turn.enemy.map.keys():
				break

			# Move one row forward.
			row += params['dir']

			# Decrease reach of piece
			tmp_reach -= 1

		return moves


	"""
  	getBwMoves(): Calculates the backward moves that a given piece can make.
  	"""
	def getBwMoves(self, params):
		moves = []

		# Calculate the first temporary row, taking into consideration the
		# direction in which the piece moves.
		row = params['row'] - params['dir']

		# Get all the positions of the pieces that belong to the player that
		# owns the piece.
		team = self.turn.map.keys()

		# Keep moving until reaching the boundaries of the board
		while row not in params['v_boundary']:

			# Create the position
			tmp_move = params['col']+str(row)
			
			# Stop if there is someone of the same team
			if tmp_move in team:
				break

			# Otherwise, you can move to this position
			moves.append(tmp_move)

			# If the position is occupied by enemy piece, stop.
			if tmp_move in self.turn.enemy.map.keys():
				break

			# Move one row backwards.
			row -= params['dir']
			
		return moves


	"""
  	getLeMoves(): Calculates the moves that a given piece can make to the left.
  	"""
	def getLeMoves(self, params):
		moves = []
		col = self.addToChar(params['col'], -params['dir'])

		# Get all the positions of the pieces that belong to the player that
		# owns the piece.
		team = self.turn.map.keys()

		# Keep moving until reaching the boundaries of the board
		while col not in params['h_boundary']:

			# Create the position
			tmp_move = col+str(params['row'])
			
			# Stop if there is someone of the same team
			if tmp_move in team:
				break

			# Otherwise, you can move to this position
			moves.append(tmp_move)

			# If the position is occupied by enemy piece, stop.
			if tmp_move in self.turn.enemy.map.keys():
				break

			# Move one row left.
			col = self.addToChar(col,-params['dir'])
			
		return moves
	
	"""
  	getRiMoves(): Calculates the moves that a given piece can make to the right.
  	"""
	def getRiMoves(self, params):
		moves = []
		col = self.addToChar(params['col'], params['dir'])

		# Get all the positions of the pieces that belong to the player that
		# owns the piece.
		team = self.turn.map.keys()

		# Keep moving until reaching the boundaries of the board
		while col not in params['h_boundary']:

			# Create the position
			tmp_move = col+str(params['row'])
			
			# Stop if there is someone of the same team
			if tmp_move in team:
				break

			# Otherwise, you can move to this position
			moves.append(tmp_move)

			# If the position is occupied by enemy piece, stop.
			if tmp_move in self.turn.enemy.map.keys():
				break

			# Move one row right.
			col = self.addToChar(col,params['dir'])
			
		return moves
	
	"""
  	getFwDMoves(): Calculates the moves that a given piece can make in a forward Diagonal.
  	"""
	def getFwDMoves(self, params):
		moves = []

		# Get all the positions of the pieces that belong to the player that
		# owns the piece.
		team = self.turn.map.keys()

		# UP
		row = params['row'] + 1
		col = self.addToChar(params['col'], 1)
		tmp_reach = 1 if type(params['piece']) is pieces.Pawn else params['reach']

		# Keep moving until reaching the boundaries of the board
		while row not in params['v_boundary'] and col not in params['h_boundary'] and tmp_reach != 0:

			# Create the position
			tmp_move = col+str(row)
			
			# Stop if there is someone of the same team
			if tmp_move in team:
				break

			# Otherwise, you can move to this position
			moves.append(tmp_move)
			
			# If the position is occupied by enemy piece, stop.
			if tmp_move in self.turn.enemy.map.keys():
				break

			# If the position is not occupied by enemy piece
			# and the piece is a Pawn, it cannot move in diagonal.
			elif type(params['piece']) is pieces.Pawn:
				moves.pop()

			# Move one row up and one column right.
			col = self.addToChar(col, 1)
			row += 1
			tmp_reach -= 1

		# Reset positions
		row = params['row'] - 1
		col = self.addToChar(params['col'], -1)
		tmp_reach = 0 if type(params['piece']) is pieces.Pawn else params['reach']
		
		# Going Down
		# Keep moving until reaching the boundaries of the board
		while row not in params['v_boundary'] and col not in params['h_boundary'] and tmp_reach != 0:

			# Create the position
			tmp_move = col+str(row)
			
			# Stop if there is someone of the same team
			if tmp_move in team:
				break

			# Otherwise, you can move to this position
			moves.append(tmp_move)
			
			# If the position is occupied by enemy piece, stop.
			if tmp_move in self.turn.enemy.map.keys():
				break

			# Move one row down and one column left.
			col = self.addToChar(col, -1)
			row -= 1
			tmp_reach -= 1

		return moves
	
	"""
  	getBwDMoves(): Calculates the moves that a given piece can make in a backward Diagonal.
  	"""
	def getBwDMoves(self, params):
		moves = []

		# Get all the positions of the pieces that belong to the player that
		# owns the piece.
		team = self.turn.map.keys()

		# UP
		row = params['row'] + 1
		col = self.addToChar(params['col'], -1)
		tmp_reach = 1 if type(params['piece']) is pieces.Pawn else params['reach']

		# Keep moving until reaching the boundaries of the board
		while row not in params['v_boundary'] and col not in params['h_boundary'] and tmp_reach != 0:

			# Create the position
			tmp_move = col+str(row)
			
			# Stop if there is someone of the same team
			if tmp_move in team:
				break

			# Otherwise, you can move to this position
			moves.append(tmp_move)
			
			# If the position is occupied by enemy piece, stop.
			if tmp_move in self.turn.enemy.map.keys():
				break

			# If the position is not occupied by enemy piece
			# and the piece is a Pawn, it cannot move in diagonal.
			elif type(params['piece']) is pieces.Pawn:
				moves.pop()

			# Move one row up and one column left.
			col = self.addToChar(col, -1)
			row += 1
			tmp_reach -= 1
		
		# Reset positions
		row = params['row'] - 1
		col = self.addToChar(params['col'], 1)
		tmp_reach = 0 if type(params['piece']) is pieces.Pawn else params['reach']

		# Going Down
		# Keep moving until reaching the boundaries of the board
		while row not in params['v_boundary'] and col not in params['h_boundary'] and tmp_reach != 0:

			# Create the position
			tmp_move = col+str(row)

			# Stop if there is someone of the same team
			if tmp_move in team:
				break

			# Otherwise, you can move to this position
			moves.append(tmp_move)
			
			# If the position is occupied by enemy piece, stop.
			if tmp_move in self.turn.enemy.map.keys():
				break

			# Move one row down and one column right.
			col = self.addToChar(col, 1)
			row -= 1
			tmp_reach -= 1
			
		return moves


	"""
  	getCrMoves(): Calculates the moves that a given piece can make in a circle-type of shape.
  	"""
	def getCrMoves(self, params):
		moves = []
		tmp_moves =[]

		# Get all the positions of the pieces that belong to the player that
		# owns the piece.
		team = self.turn.map.keys()

		# x will represent the columns
		x = params['col']

		# y will represent the rows
		y = params['row']

		# The pawn can move 2+1:

		# 2 columns in either side and 1 row in either side
		vertical = [[self.addToChar(x, -2), self.addToChar(x, 2)],[y-1, y+1]]

		# 1 column in either side and 2 rows in either side
		horizontal = [[self.addToChar(x, -1), self.addToChar(x, 1)],[y-2, y+2]]

		# Create the positions
		# By multiplying the possibilites
		tmp_moves.extend( list(itertools.product(vertical[0], vertical[1])) )
		tmp_moves.extend( list(itertools.product(horizontal[0], horizontal[1])) )

		# Check each move is valid
		for m in tmp_moves:

			c = m[0]
			r = m[1]

			# Should be insed of the horizontal boundaries
			if c <= params['h_boundary'][0] or c >= params['h_boundary'][1]:
				continue
			
			# Should be insed of the vertical boundaries
			if r >= params['v_boundary'][0] or r <= params['v_boundary'][1]:
				continue

			# If there is someone of the same team
			if c+str(r) not in team:
				# Otherwise, you can move to this position
				moves.append(c+str(r))
			
		return moves