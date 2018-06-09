from random import *

class Die(object):

	def __init__(self, number_of_faces):
		self._faces = number_of_faces
		self._current_face = 1

	def roll(self):
		self._current_face = randint(1, self.face_count)

	@property 
	def face_count(self):
		return self._faces

	@property
	def current_face(self):
		return self._current_face

	@staticmethod
	def create_die(number_of_faces):
		die = Die(number_of_faces)
		return die
