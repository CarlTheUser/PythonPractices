from Die import Die
from DiePlayer import DiePlayer
from DieGame import DieGame

computer1 = DiePlayer("Computer 1")
computer2 = DiePlayer("Computer 2")
computer3 = DiePlayer("Computer 3")

die = Die.create_die(6)

game = DieGame(20, die)
game.start_game([computer1, computer2, computer3])

print("{} won with final score of: {}".format(game.winner.name, str(game.winner.score)))