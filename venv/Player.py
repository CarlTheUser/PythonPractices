from ScoreListener import ScoreListener
from abc import ABCMeta, ABC
class Player(ABC):

	__metaclass__ = ABCMeta

	def __init__(self, name):
		self._name = name
		self._score = 0
		self._score_listener = None

	@property
	def name(self): 
		return self._name

	@property
	def score(self):
		return self._score

	@name.setter 
	def name(self, new_name):
		self._name = new_name

	@property
	def scoreListener(self):
		return self._score_listener

	@scoreListener.setter
	def scoreListener(self, new_score_listener):
		self._score_listener = new_score_listener