from abc import ABC, ABCMeta, abstractmethod

class GuessWordCharacter(ABC):

    def __init__(self, value, mask):
        self._value = value
        self._mask = mask

    @property
    def value(self):
        return self._value

    @property
    def mask(self):
        return self._mask

    @abstractmethod
    def needs_guessing(self):
        pass

    @abstractmethod
    def get_display_value(self):
        pass

    @abstractmethod
    def evaluate(self, character):
        pass

    @staticmethod
    def create_character(character):
        c = str(character)[0]
        return _GuessableCharacter(c, '_') if str(c).isalnum() else _StaticCharacter(c)

class _GuessableCharacter(GuessWordCharacter):

    def __init__(self, value, mask):
        super().__init__(value, mask)
        self._is_guessed = False

    def needs_guessing(self):
        return not self._is_guessed

    def get_display_value(self):
        return self.value if self._is_guessed else self.mask

    def evaluate(self, character):
        if not self._is_guessed:
            upper_self = str(self.value).upper()
            upper_other = str(character).upper()
            self._is_guessed = upper_self == upper_other
        return self._is_guessed

class _StaticCharacter(GuessWordCharacter):

    def __init__(self, value):
        super().__init__(value, value)

    def needs_guessing(self):
        return False

    def get_display_value(self):
        return self.value

    def evaluate(self, character):
        return False