import unittest
from Pynigma.scrambler import Scrambler

class ScramblerTests(unittest.TestCase):

    def test_scrambler_instantiation(self):
        scrambler = Scrambler('123', 'AAA')

    def test_scramble_and_unscramble_single_letter(self):
        self.scrambler = Scrambler('123', 'AAA')
        self.scrambled = self.scrambler.scramble('A')
        self.assertEquals('F', self.scrambled)

        self.scrambler = Scrambler('123', 'AAA')
        self.scrambled = self.scrambler.unscramble('F')
        self.assertEquals('A', self.scrambled)

    def test_scramble_and_unscramble_string(self):
        self.scrambler = Scrambler('123', 'AAA')
        scrambled = ''
        for letter in 'String':
            scrambled += self.scrambler.scramble(letter)
        self.assertEquals('YQKRCJ', scrambled)

        unscrambled = ''
        self.scrambler = Scrambler('123', 'AAA')
        for letter in 'YQKRCJ':
            unscrambled += self.scrambler.unscramble(letter)
        self.assertEquals('STRING', unscrambled)