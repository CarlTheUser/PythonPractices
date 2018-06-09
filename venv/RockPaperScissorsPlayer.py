from abc import ABCMeta, abstractmethod 
from Player import Player
from RockPaperScissorsOption import RockPaperScissorsOption
from random import *

class RockPaperScissorsPlayer(Player):
    
	__metaclass__ = ABCMeta

	def __init__(self, name):
		super().__init__(name)
		self._last_option = None

	def increment_score(self):
		self._score += 1
		if self._score_listener != None:
			self._score_listener.onPlayerScored(self, 1)

	@property
	def last_option(self):
		return self._last_option

	@abstractmethod
	def take_turn(self):
		pass

class NonComputerRockPaperScissorsPlayer(RockPaperScissorsPlayer):

	def __init__(self, name):
		super().__init__(name)

	def take_turn(self):
		option = None
		try:
			choice = int(input("1. Rock \n2. Paper \n3. Scissors\nchoice:"))
			if choice == 1:
				option = RockPaperScissorsOption.ROCK_OPTION
			elif choice == 2:
				option = RockPaperScissorsOption.PAPER_OPTION
			elif choice == 3:
				option = RockPaperScissorsOption.SCISSORS_OPTION
			else:
				print("Invalid option\n")
				option = self.take_turn()
		except ValueError:
			print("Invalid input\n")
			option = self.take_turn()
		self._last_option = option
		return self.last_option

class ComputerRockPaperScissorsPlayer(RockPaperScissorsPlayer):
	INSTANCE_COUNT = 1

	def __init__(self):
		name = "Computer {}".format(str(ComputerRockPaperScissorsPlayer.INSTANCE_COUNT))
		ComputerRockPaperScissorsPlayer.INSTANCE_COUNT += 1
		super().__init__(name)


	def take_turn(self):
		option = None
		randomNumber = randint(1, 3)
		if randomNumber == 1:
			option = RockPaperScissorsOption.ROCK_OPTION
		elif randomNumber == 2:
			option = RockPaperScissorsOption.PAPER_OPTION
		elif randomNumber == 3:
			option = RockPaperScissorsOption.SCISSORS_OPTION
		self._last_option = option
		return self.last_option
		