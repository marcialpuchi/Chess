from player import Player
from moves import Moves

class Board(Moves):

	"""
	The Board class allows the players to setup the game by creating
	the necessary set of pieces needed for each player.

	It also extends the class Moves, in which all the allowed moves
	are calculated based on the current position of all the pieces that
	exist on the board at a given point in time.

	The Board class includes the following elements:
		- player: a 2-dimensional array that contains all the pieces
				  of the board, grouped by player.
		- turn: It controls which player turn is the current one.
		
	"""
	
	def __init__(self):
		Moves.__init__(self)


		self.p1 = Player('white', 'down')
		self.p2 = Player('black', 'up')

		self.p1.enemy = self.p2
		self.p2.enemy = self.p1
		
		self.turn = self.p1


	"""
	getMap(): creates a dictionary that contains all the pieces on the board
			  and uses its positions as keys.

			  This function allows to draw the board in conbination with the
			  chess_ui class.
	"""
	def getSimpleMap(self):
		return dict((k, p.short) for k, p in self.getFullMap().iteritems())


	"""
	getPlayerMap(): creates a set that contains all the pieces on the board.
	"""
	def getFullMap(self):
		fullMap = self.p1.map.copy()
		fullMap.update(self.p2.map)
		return fullMap	