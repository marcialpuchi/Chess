class Rules(object):
	
	def __init__(self, board, origin, target):
		self.board = board
		self.origin = origin
		self.target = target

		self.king_pos, self.king = board.turn.getKing()
		
		self.player = board.turn
		self.player_attacks = board.attackPositions(self.player)

		self.enemy = board.turn.enemy
		self.enemy_attacks = board.attackPositions(self.enemy)

		self.piece = None
		
	def validateMove(self):
		
		if self.exists() is False:
			print "Doesn't exists"
			return False

		if self.isValidMove() is False:
			print "Invalid move"
			return False

		if self.isTargetCheck() is True:
			print "Is checked"
			return False

		return True

	def exists(self):
		if self.origin in self.player.map.keys():
			self.piece = self.player.map[self.origin]
			return True

		return False

	def isValidMove(self):
		if self.target in self.board.getAvailableMoves(self.origin):
			return True
		return False

	def isTargetCheck(self):
		if self.king_pos == self.origin and self.target in self.enemy_attacks:
			return True
		return False

	def isCheck(self):
		if self.king_pos in self.enemy_attacks:
			return True
		return False
