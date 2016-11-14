import unittest
from Pynigma.rotor import Rotor


class RotorTests(unittest.TestCase):

    def test_rotor_instantiation(self):
        rotor = Rotor(1)


    def test_rotor_values(self):
        rotor = Rotor(1)
        a_connection = rotor.get_connection('A')
        b_connection = rotor.get_connection('B')
        c_connection = rotor.get_connection('C')

        self.assertEquals(a_connection, 'E')
        self.assertEquals(b_connection, 'K')
        self.assertEquals(c_connection, 'M')