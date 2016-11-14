import unittest
import datetime
from Pynigma.key_reader import KeyReader
from Pynigma.scrambler import Scrambler


class ScramblerTests(unittest.TestCase):

    def test_scrambler_instantiation(self):
        keys = KeyReader('../keys.txt')
        rotor_order = keys.get_rotor_order(datetime.datetime.now().date())
        scrambler = Scrambler(rotor_order)
