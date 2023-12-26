class MaskConstants:
    BLACK = 0
    YELLOW = 1
    GREEN = 2


class Mask:
    BLACK = MaskConstants.BLACK  # wrong letter
    YELLOW = MaskConstants.YELLOW  # correct letter but in a wrong spot
    GREEN = MaskConstants.GREEN  # correct letter in the correct spot

    def __init__(self, num1=BLACK, num2=BLACK, num3=BLACK, num4=BLACK, num5=BLACK):
        self.num1 = num1
        self.num2 = num2
        self.num3 = num3
        self.num4 = num4
        self.num5 = num5

    @staticmethod
    def change_str(str, old_letter, new_letter):
        """The function is designed to replace a specific character in a given string with a new character"""
        index_to_change = str.index(old_letter)
        new_str = str[:index_to_change] + new_letter + str[index_to_change + 1:]
        return new_str

    @staticmethod
    def compute_from(word, target):
        """
        Compute mask describing a given word, given a target word.
        :param word: str
        :param target: str
        :return: Mask
        """
        index_of_letter = 0

        # loop for correct letter in the correct spot
        for letter in word:
            if letter == target[index_of_letter]:
                word = word[:index_of_letter] + "*" + word[index_of_letter + 1:]  # in order to mark (GREEN)
                target = target[:index_of_letter] + "*" + target[index_of_letter + 1:]  # in order to mark (GREEN)
            index_of_letter += 1

        index_of_letter = 0

        # loop for correct letter but in a wrong spot
        for letter in word:
            if letter == "*":
                index_of_letter += 1
                continue
            if letter in target:
                word = word[:index_of_letter] + "@" + word[index_of_letter + 1:]  # in order to mark (YELLOW)
                target = Mask.change_str(target, letter, "@")
                index_of_letter += 1
            else:
                index_of_letter += 1

        mask_list = []
        for letter in word:
            if letter.isalpha():
                mask_list.append(Mask.BLACK)
            elif letter == "@":  # YELLOW
                mask_list.append(Mask.YELLOW)
            elif letter == "*":  # GREEN
                mask_list.append(Mask.GREEN)
        return Mask(mask_list[0], mask_list[1], mask_list[2], mask_list[3], mask_list[4])