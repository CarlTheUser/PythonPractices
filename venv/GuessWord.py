from abc import ABC, abstractmethod
from GuessWordCharacter import GuessWordCharacter
class GuessWord(object):

    def __init__(self, guess_word, clues = []):
        self._guest_word = guess_word
        self._clues = clues
        self._listener = None
        self._guess_word_characters = []
        for character in guess_word:
            self._guess_word_characters.append(GuessWordCharacter.create_character(character))

    def guess_character(self, character):
        characters_matched = 0
        needs_more_guessing = False
        break_needs_more_guessing = False
        for guess_character in self._guess_word_characters:
            if guess_character.needs_guessing() and guess_character.evaluate(character):
                characters_matched += 1
            if not break_needs_more_guessing:
                needs_more_guessing = guess_character.needs_guessing()
                if needs_more_guessing:
                    break_needs_more_guessing = True
        if not needs_more_guessing:
            if self._listener != None:
                self._listener.on_word_guessed(self.guess_word)
        return characters_matched

    def guess_word_display_value(self):
        display_value = str()
        for character in self._guess_word_characters:
            display_value += character.get_display_value()
        return display_value

    @property
    def guess_word(self):
        return self._guest_word

    @property
    def clues(self):
        return self._clues

    @property
    def listener(self):
        return self._listener

    @listener.setter
    def listener(self, new_listener):
        self._listener = new_listener
        return new_listener

class Listener(ABC):

    @abstractmethod
    def on_word_guessed(self, word):
        pass