from GuessWordCharacter import GuessWordCharacter
from GuessWord import  GuessWord
from GuessWordGame import GuessWordGame
from random import *

guess_word_map = {}

guess_word_map["corned beef"] = ["Food", "Eaten with rice", "From cow"]
guess_word_map["rubber band"] = ["elastic", "colorful"]
guess_word_map["laptop"] = ["common wit I.T.", "device", "can be used to code"]
guess_word_map["java"] = ["common wit I.T.", "programming language", "object oriented"]

keys = list(guess_word_map.keys())
random_index = randrange(0,len(keys))

word_to_guess = keys[random_index]

guess_word_game = GuessWordGame(len(word_to_guess))

guess_word_game.start_game(word_to_guess, guess_word_map[word_to_guess])

if guess_word_game.player_won:
    print("You guessed the word {} under {} tries".format(guess_word_game.word_to_guess, str(guess_word_game.current_guess_count)))
else:
    print("You failed to guess the word {}".format(guess_word_game.word_to_guess))


