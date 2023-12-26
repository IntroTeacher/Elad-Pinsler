from mask import Mask


class Stack:

    def __init__(self, list_of_words):
        self.list_of_words = list_of_words

    def filter(self, word_input, mask):
        """
        filter all words in the stack that does not fit to the mask.
        :param word_input: str
        :param mask: Mask
        """
        list_of_chosen_words = []
        for word in self.get_words():
            chosen_mask = Mask.compute_from(word, word_input)
            if chosen_mask.num1 == mask.num1 and chosen_mask.num2 == mask.num2\
                    and chosen_mask.num3 == mask.num3 and chosen_mask.num4 == mask.num4\
                    and chosen_mask.num5 == mask.num5:
                list_of_chosen_words.append(word)
        return Stack(list_of_chosen_words)

    def get_words(self):
        """function that returns a list of the words in the stack"""
        return list(self.list_of_words)

    def __len__(self):
        """Creates and returns the len of the Stack"""
        return len(self.list_of_words)

    def __iter__(self):
        """Creates and returns an iterator of the stack"""
        return iter(self.list_of_words)