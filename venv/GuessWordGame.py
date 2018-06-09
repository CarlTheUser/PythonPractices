from GuessWordCharacter import  GuessWordCharacter
from GuessWord import GuessWord, Listener

class GuessWordGame(Listener):

    def __init__(self, max_guess_count):
        self._max_guess_count = max_guess_count
        self._word_to_guess = None
        self._current_guess_count = 0
        self._is_game_finished = False
        self._player_won = False

    def start_game(self, word_to_guess, clues = []):
        guess_word = GuessWord(word_to_guess, clues)
        self._word_to_guess = word_to_guess
        guess_word.listener = self

        while not self._is_game_finished and self.current_guess_count < self._max_guess_count:
            remaining_guesses = self._max_guess_count - self.current_guess_count
            print("Guess the word: \n{}\nGuesses remaining: {}".format(guess_word.guess_word_display_value(), str(remaining_guesses)))
            print("Clues:\n")
            for clue in clues:
                print(clue)

            guess_character = input("Your guess: ")[0]

            guessed_characters = int(guess_word.guess_character(guess_character))

            print("guessed {} character/s.".format(str(guessed_characters)) if guessed_characters > 0 else "No character {} in the word.".format(guess_character) )

            self._current_guess_count += 1



    def on_word_guessed(self, word):
        self._is_game_finished = True
        self._player_won = True


    @property
    def word_to_guess(self):
        return self._word_to_guess

    @property
    def current_guess_count(self):
        return self._current_guess_count

    @property
    def max_guess_count(self):
        return self._max_guess_count

    @property
    def player_won(self):
        return self._player_won