from RockPaperScissorsPlayer import RockPaperScissorsPlayer, NonComputerRockPaperScissorsPlayer, ComputerRockPaperScissorsPlayer
from RockPaperScissorsOption import RockPaperScissorsOption
from RockPaperScissorsGame import RockPaperScissorsGame

player = NonComputerRockPaperScissorsPlayer(input("What is your name?\nname: "))
computer1 = ComputerRockPaperScissorsPlayer()
game = RockPaperScissorsGame(10)

game.start_game([player, computer1])

print("The winner is: {} with final score of {}".format(game.winner.name, str(game.winner.score)))

#print("{} score: {}".format(player.name, player.score))

#player.increment_score()

#print("{} score: {}".format(player.name, player.score))

#option = player.take_turn()
#print("{} is defeated by: {}".format(option.name, option._defeated_by.name))
