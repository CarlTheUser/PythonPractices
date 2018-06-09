from abc import ABC, ABCMeta, abstractmethod
import sys

class Operation(ABC):
	__metaclass__ = ABCMeta

	EXIT = None

	def __init__(self, name):
		self.name = name

	@abstractmethod
	def operate(self):
		pass


class ExitOperation(Operation):

	def __init__(self):
		super().__init__("Exit")

	def operate(self):
		print("Exiting...")
		sys.exit()

Operation.EXIT = ExitOperation()