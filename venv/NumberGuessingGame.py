from random import *


class NumberGuessingGame(object):
    
	def __init__(self, max_guess):
		self._max_guess = max_guess
		self._current_guesses = 0
		self._guess_number = 0
		self._player_won = False

	def start_game(self, low, high):
		self._guess_number = randint(low, high)
		distance_from_high = high - self._guess_number
		distance_from_low = self._guess_number - low
		near_range = (distance_from_high / 2) if distance_from_high < distance_from_low else (distance_from_low / 2)
		near_range = abs(near_range)
		print("Guess a number between {} and {}.\n".format(str(low), str(high)))

		while self.number_of_guesses < self._max_guess and not self.player_won:
			remaining_guesses = self._max_guess - self._current_guesses
			print("You have {} more guesses.\n".format(str(remaining_guesses)))
			try:
				guess = int(input("Guess the number: "))
				self._current_guesses += 1
				if guess == self.guess_number:
					print("Correct guess!")
					self._player_won = True
				elif guess > high:
					print("Number is greater than high.\n")
				elif guess < low:
					print("Number is lower than low.\n")
				elif guess >= self.guess_number - near_range and guess <= self.guess_number + near_range:
					print("Almost there.")
				else:
					print("Wrong guess :(\n")
			except ValueError:
				print("Unacceptable input.\n")


	@property 
	def guess_number(self):
		return self._guess_number

	@property
	def player_won(self):
		return self._player_won

	@property
	def number_of_guesses(self):
		return self._current_guesses