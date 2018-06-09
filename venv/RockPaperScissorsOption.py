class RockPaperScissorsOption():

	def __init__(self, name):
		self._name = name
		self._defeated_by = None

	@property
	def name(self):
		return self._name

	def is_defeated_by(self, option):
		return self._defeated_by == option
	
	ROCK_OPTION = None
	PAPER_OPTION = None
	SCISSORS_OPTION = None

RockPaperScissorsOption.ROCK_OPTION = RockPaperScissorsOption("Rock")
RockPaperScissorsOption.PAPER_OPTION = RockPaperScissorsOption("Paper")
RockPaperScissorsOption.SCISSORS_OPTION = RockPaperScissorsOption("Scissors")

RockPaperScissorsOption.ROCK_OPTION._defeated_by = RockPaperScissorsOption.PAPER_OPTION
RockPaperScissorsOption.PAPER_OPTION._defeated_by = RockPaperScissorsOption.SCISSORS_OPTION
RockPaperScissorsOption.SCISSORS_OPTION._defeated_by = RockPaperScissorsOption.ROCK_OPTION
	

