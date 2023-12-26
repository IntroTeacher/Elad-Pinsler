import itertools
import stack
import numpy
from mask import MaskConstants
from stack import Stack


class HeuristicWordleSolver:

    def __init__(self, wordle):
        self.wordle = wordle
        self.stack = stack.Stack(wordle.dataset)

    @staticmethod
    def all_masks():
        """
        function that creates all the masks that can be made
        :return: list of lists
        """
        values = [MaskConstants.BLACK, MaskConstants.YELLOW, MaskConstants.GREEN]
        return [list(outcome) for outcome in itertools.product(values, repeat=5)]

    def choose_word(self):
        """
        This function chooses the word that minimizes the stack of the remaining relevant words
        :return: str
        """
        if self.wordle.tries == 6:
            return "crane"
        word_with_minimal_variance = self.stack.get_words()[0]
        minimal_variance = None
        for word in self.stack.get_words():
            list_of_stacks_sizes = []
            all_masks = self.all_masks()
            for chosen_mask in all_masks:
                chosen_stack = Stack.filter(self.stack, word, chosen_mask)
                list_chosen_stack = chosen_stack.get_words()
                if len(list_chosen_stack) != 0:
                    length_of_chosen_stack = len(chosen_stack)
                    list_of_stacks_sizes.append(length_of_chosen_stack)
            variance = numpy.var(list_of_stacks_sizes)

            if minimal_variance is None:
                minimal_variance = variance

            if variance < minimal_variance:
                minimal_variance = variance
                word_with_minimal_variance = word
        return word_with_minimal_variance

    def play_step(self):
        """
        The function plays a single step in the game
        :return:
        """
        word_chosen = self.choose_word()
        dataset = self.wordle.dataset
        mask_of_target = self.wordle.guess(word_chosen)
        self.wordle.dataset = stack.Stack(dataset).filter(self.wordle.solution, mask_of_target)

    def won_game(self):
        """
        function that returns whether the game has been won or not
        """
        if self.choose_word() == self.wordle.solution:
            return True
        return False

    def lost_game(self):
        """
        function that returns whether the game has been lost or not.
        :return:
        """
        return self.wordle.lost_game()
