from longest_word.game import Game
import string
import unittest

# tests/test_game.py
class TestGame:
    def test_game_initialization(self):
            # setup
            game = Game()
            # exercise
            grid = game.grid
            # verify
            assert type(grid) == list
            assert len(grid) == 9

            for item in grid:
                print(f'{item}')
                assert item in string.ascii_uppercase
            # teardown

    def test_empty_word_is_invalid(self):
            # setup
            game = Game()
            # exercise
            result = game.is_valid('')
            # verify
            assert result == False

    def test_valid_word_is_valid(self):
        # setup
        test_grid = 'TESTING12'
        test_word = '12TESTING'
        game = Game()
        game.grid = list(test_grid)

        # exercise
        result = game.is_valid(test_word)
        # verify
        assert result == True

    def test_invalid_word(self):
        # setup
        test_grid = 'TESTING12'
        test_word = 'SOMENUMBERS'
        game = Game()
        game.grid = list(test_grid)

        # exercise
        result = game.is_valid(test_word)
        # verify
        assert result == False



            #teardown
