from Die import Die
from DiePlayer import DiePlayer
from ScoreListener import ScoreListener
class DieGame(ScoreListener):

	def __init__(self, max_score, die):
		self._max_score = max_score
		self._die = die
		self._has_winner = False
		self._winner = None


	def start_game(self, players = []):
		for player in players:
			player.scoreListener = self
		round = 1
		while not self._has_winner:
			print("round {}\n".format(str(round)))
			round += 1
			for player in players:
				if self._has_winner:
					break
				print("{}'s turn...".format(player.name))
				player.roll_die(self._die)
				print("{} rolled the die and got the score of {}; current score: {}".format(player.name, str(self._die.current_face), str(player.score)))

	@property 
	def winner(self):
		return self._winner


	def onPlayerScored(self, player, scoredPoints):
		if player.score >= self._max_score:
			self._has_winner = True
			self._winner = player


