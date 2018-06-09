from NumberGuessingGame import NumberGuessingGame

game = NumberGuessingGame(10)

game.start_game(1, 100)

if game.player_won:
	print("You guessed the number {} under {} guesses.\n".format(str(game.guess_number), str(game.number_of_guesses)))
else:
	print("Try again next time. The number was {}.\n".format(str(game.guess_number)))