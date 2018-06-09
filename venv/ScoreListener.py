from abc import ABC, ABCMeta, abstractmethod
class ScoreListener(ABC):
    
	__metaclass__ = ABCMeta

	@abstractmethod
	def onPlayerScored(self, player, scoredPoints):
		pass


