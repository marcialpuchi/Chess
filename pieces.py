class Piece(object):
	
	""" 
	The class piece can be any chess piece.
	All the pieces in chess should have a:
		
		- Name: Describes the type of piece this is.
		- ID: A short name which will represent this piece on the board.
		- color: specifies the player who owns this particular piece.
		- Reach: specifies the amount of squares that this piece can move.
		- Directions: A set of possible directions in which this piece is 
					  allowed to move.
	"""

	def __init__(self, name, id, color):

		self.name = name
		self.player = color[0] 
		self.id = id
		self.short = self.player+self.id
		self.color = color
		self.move_count = 0

		self.reach = 0
		self.directions = {
			'fw':False,
			'bw':False,
			'le':False,
			'ri':False,
			'ld':False,
			'rd':False
		}
		

	def getName(self):
		return self.name

	def getColor(self):
		return self.color

	def getDirections(self):
		return [k for k, v in self.directions.iteritems() if v]

	def updateCount(self, count):
		self.move_count += count


	def __str__(self):
		return self.color + " " + self.name + " @ " + self.pos


class King(Piece):

	""" 
	The King is a class that inherits the properties of its parent class Piece and
	modifies its properties to fit its particular requirements.

	A King is allowed to:
		- Reach: 1 square away from its original position.
		- Directions: It is allowed to move in any direction.
		- Checked: This property is unique to the King, if this variable is
				   set to True, the only moves available will be retricted to
				   those that are able to change the state of this variable.

	"""

	def __init__(self, color):
		Piece.__init__(self, 'king', 'K', color)
		self.reach = 1
		self.checked = False
		self.directions.update(dict.fromkeys(self.directions.iterkeys(), True))

		def check(self, current_pos, target_pos):
			cur_pos = list(current_pos)
			tar_pos = list(target_pos)

			""" target should be 1 away """

class Queen(Piece):

	""" 
	The Queen is a class that inherits the properties of its parent class Piece 
	
	A Queen is allowed to:
		- Reach: It has no restrictions on the amount of squares that can move
		- Directions: It is allowed to move in any direction.
	"""

	def __init__(self, color):
		Piece.__init__(self, 'queen', 'Q', color)
		self.reach = -1
		self.directions.update(dict.fromkeys(self.directions.iterkeys(), True))
	

class Rook(Piece):

	""" 
	The Rook is a class that inherits the properties of its parent class Piece
	
	A Rook is allowed to:
		- Reach: It has no restrictions on the amount of squares that can move
				 is in a straight horizontal or vertical line.
		- Directions: It is allowed to move in any horizontal or vertical direction.
		
	"""

	def __init__(self, color):
		Piece.__init__(self, 'rook','R',  color)
		self.reach = -1
		self.directions.update(dict.fromkeys(['fw','bk','le','ri'], True))

class Bishop(Piece):

	""" 
	The Bishop is a class that inherits the properties of its parent class Piece

	A Bishop is allowed to:
		- Reach: It has no restrictions on the amount of squares that can move
		- Directions: It is allowed to move in diagonal moves.
	"""

	def __init__(self, color):
		Piece.__init__(self, 'bishop','B',  color)
		self.reach = -1
		self.directions.update(dict.fromkeys(['ld','rd'], True))

class Knight(Piece):

	"""
	The Knight is a class that inherits the properties of its parent class Piece
	A Knight is allowed to:
		- Reach: It can reach 2+1 squares.
		- Directions: It is allowed to move in any horizontal or vertical direction.
	"""

	def __init__(self, color):
		Piece.__init__(self, 'knight', 'N', color)
		self.directions = {'cr': True}

class Pawn(Piece):

	""" 
	The Pawn is a class that inherits the properties of its parent class Piece
	
	A Pawn is allowed to:
		- Reach: 1 square away from its original position.
		- Directions: It can move up to 2 squares forward in the first move and
					  only 1 after that. It is only allowed to attack pieces that
					  are one square away in diagonal.

		- updateCount(): It changes the reach to 1 after the first move.

		- promote(): The Pawn can be promoted if it reaches into any other type of piece
				   (except the King), when it reaches the last row opposite to its
				   original location.
	"""

	def __init__(self, color):
		Piece.__init__(self, 'pawn', 'P', color)
		self.reach = 2
		self.directions.update(dict.fromkeys(['fw','ld','rd'], True))

	def updateCount(self, count):

		self.move_count += count

		if self.move_count > 0:
			self.reach = 1

	def promote(self, rank):
		pass

