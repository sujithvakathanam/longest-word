""" Game Module """
import random
import string

""" Game Class """
class Game:
    def __init__(self) -> list:
        """Attribute a random grid to size 9"""
        self.grid = []
        for _ in range(9):
            self.grid.append(random.choice(string.ascii_uppercase))


    def is_valid(self, word: str) -> bool:
        """Return True if and only if the word is valid, given the Game's grid"""
        for item in list(word):
            if item not in self.grid:
                return False
        if len(word) == 0:
            return False
        return True

if __name__== 'main':
    game = Game()
    print(game.grid) # --> OQUWRBAZE
    MY_WORD = "BAROQUE"
    game.is_valid(MY_WORD) # --> True
