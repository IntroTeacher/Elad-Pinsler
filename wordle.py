import json
from mask import Mask

with open('words.json', 'r') as file:
    words_data = json.load(file)


class Wordle:

    def __init__(self, solution, dataset):
        self.solution = solution
        self.tries = 6
        if dataset is not None:
            self.dataset = dataset
        else:
            self.dataset = words_data
        self.mask = Mask()

    def restart(self, solution=None):
        """
        Initialize the game to a new game
        :param solution: str (optional)
        """
        if solution is not None:
            self.solution = solution
        self.tries = 6

    def guess(self, word):
        """
        Handles a guess from the user (str) and return a mask object representing a feedback to the user based on his guess.
        :param word: str
        :return: Mask
        """
        self.tries -= 1
        return self.mask.compute_from(word, self.solution)

    def lost_game(self):
        """Returns whether the game has been lost or not."""
        if self.tries == 0:
            return True
        return False

    def get_possible_words(self):
        """
        Returns all the possible words for guessing
        :return: lst
        """
        return self.dataset
