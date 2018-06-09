from RockPaperScissorsPlayer import RockPaperScissorsPlayer
from ScoreListener import ScoreListener
class RockPaperScissorsGame(ScoreListener):
    
	def __init__(self, max_score):
		self._max_score = max_score
		self._has_winner = False
		self._winner = None

	@property 
	def winner(self):
		return self._winner

	def start_game(self, players = []):
		if len(players) == 0:
			return
		for player in players:
			player.scoreListener = self
		round = 0
		while not self._has_winner :
			round += 1
			print("round {}".format(str(round)))
			for player in players:
				player.take_turn()
			for player in players:
				if self._has_winner:
					break
				for enemy_player in players:
					if enemy_player == player: 
						continue
					if enemy_player.last_option.is_defeated_by(player.last_option):
						player.increment_score()
						print("{}'s {} was defeated by {}'s {}.\n".format(enemy_player.name, enemy_player.last_option.name, player.name, player.last_option.name))
					elif enemy_player.last_option == player.last_option:
						print("{} and {} is draw.\n".format(player.name, enemy_player.name))
						continue
				print("{}'s score: {}".format(player.name, player.score))
	
	def onPlayerScored(self, player, scoredPoints):
		if player.score >= self._max_score:
			self._has_winner = True
			self._winner = player



