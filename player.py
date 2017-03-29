from pieces import *

class Player(object):

	def __init__(self, color, position):
		self.color = color
		self.position = position
		
		self.map = {}
		self.enemy = None
		self.moves = [None]
		self.captured = []
		self.dir = 0
		self.createSet()

	def __str__(self):
		return self.color + " player: What's your next move?"

		
	"""
	createSet(): is a function that allows the board to create a set of pieces
				 necessary for each player to start a new game.
	"""
	def createSet(self):

		# Set the order in which the pieces should be located on the board
		order=[	
				('a','R'),('b','N'),('c','B'),('d','Q'),
				('e','K'),('f','B'),('g','N'),('h','R')
			  ]

		# Depending on the color, the starting rows are selected.
		if self.position == 'down':
			rows = ['1','2']
			self.dir = 1
		else:
			rows = ['8','7']
			self.dir = -1

		# Create a piece based on the order that was set above.
		for col, pieceType in order:
			
			# Create a special piece and a pawn based on its ID's.
			specialPiece = self.createPiece(pieceType)
			pawnPiece = self.createPiece('P')

			# Place the new pieces in the pieces dictionary, using its
			# position as key.
			self.map[col + rows[0]] = specialPiece
			#self.map[col + rows[1]] = pawnPiece


	"""
	createPiece(): Allows us to create a particular class of piece using
				   its ID to select the correct type of Piece.

				   It takes 1 argument, the "type" which refers to the
				   type of piece you need to create. 
	"""
	def createPiece(self, type):
		if type == 'K':
			return King(self.color)
		elif type == 'Q':
			return Queen(self.color)
		elif type == 'R':
			return Rook(self.color)
		elif type == 'B':
			return Bishop(self.color)
		elif type == 'N':
			return Knight(self.color)
		elif type == 'P':
			return Pawn(self.color)
		else:
			return False

	"""
	getKing():  It allows to get the King piece of this player.
	"""
	def getKing(self):

		for position, piece in self.map.iteritems():
			if type(piece) is King:
				return (position, piece)


	"""
	getPiece(): allows to validate that a piece exists at a give position.

				It takes one argument "pos", that refers to the position of a
				piece on the board.
	"""
	def getPiece(self, pos):
		
		if pos in self.map.keys():
			return self.map[pos]
			
		return False
