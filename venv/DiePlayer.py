from Player import Player

class DiePlayer(Player):
	
	def __init__(self, name):
		super().__init__(name)

	def roll_die(self, die):
		die.roll()
		self._score += die.current_face
		if self.scoreListener != None:
			self.scoreListener.onPlayerScored(self, die.current_face)
	


