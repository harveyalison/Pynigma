import unittest
from Pynigma.rotor import Rotor

class RotorTests(unittest.TestCase):

    def test_rotor_instantiation(self):
        rotor = Rotor(1,'A')

    def test_rotor_1_output_values_with_ring_setting_A(self):
        rotor = Rotor(1,'A')
        a_connection = rotor.get_output('A')
        b_connection = rotor.get_output('B')
        c_connection = rotor.get_output('C')

        self.assertEquals('E', a_connection)
        self.assertEquals('K', b_connection)
        self.assertEquals('M', c_connection)

    def test_rotor_1_input_values_with_ring_setting_A(self):
        rotor = Rotor(1,'A')
        a_connection = rotor.get_input('A')
        b_connection = rotor.get_input('B')
        c_connection = rotor.get_input('C')

        self.assertEquals('U', a_connection)
        self.assertEquals('W', b_connection)
        self.assertEquals('Y', c_connection)

    def test_rotor_1_output_values_with_various_ring_settings(self):
        rotor = Rotor(1,'B')
        a_connection = rotor.get_output('A')
        b_connection = rotor.get_output('B')
        c_connection = rotor.get_output('C')

        self.assertEquals('K', a_connection)
        self.assertEquals('M', b_connection)
        self.assertEquals('F', c_connection)

        rotor = Rotor(1, 'F')
        a_connection = rotor.get_output('A')
        b_connection = rotor.get_output('B')
        c_connection = rotor.get_output('C')

        self.assertEquals('G', a_connection)
        self.assertEquals('D', b_connection)
        self.assertEquals('Q', c_connection)

        rotor = Rotor(1, 'Z')
        a_connection = rotor.get_output('A')
        b_connection = rotor.get_output('B')
        c_connection = rotor.get_output('C')

        self.assertEquals('J', a_connection)
        self.assertEquals('E', b_connection)
        self.assertEquals('K', c_connection)

    def test_rotor_1_input_values_with_various_ring_settings(self):
        rotor = Rotor(1,'B')
        a_connection = rotor.get_input('A')
        b_connection = rotor.get_input('B')
        c_connection = rotor.get_input('C')

        self.assertEquals('T', a_connection)
        self.assertEquals('V', b_connection)
        self.assertEquals('X', c_connection)

        rotor = Rotor(1, 'F')
        a_connection = rotor.get_input('A')
        b_connection = rotor.get_input('B')
        c_connection = rotor.get_input('C')

        self.assertEquals('P', a_connection)
        self.assertEquals('R', b_connection)
        self.assertEquals('T', c_connection)

        rotor = Rotor(1, 'Z')
        a_connection = rotor.get_input('A')
        b_connection = rotor.get_input('B')
        c_connection = rotor.get_input('C')

        self.assertEquals('V', a_connection)
        self.assertEquals('X', b_connection)
        self.assertEquals('Z', c_connection)

    def test_rotate_method(self):
        list = [1,2,3,4,5]
        rotor = Rotor(1, 'A')
        rotor.rotate(list, 1)
        self.assertEquals([5,1,2,3,4], list)
        rotor.rotate(list, -1)
        self.assertEquals([1,2,3,4,5], list)
        rotor.rotate(list, 3)
        self.assertEquals([3,4,5,1,2], list)
        list = ['a','b','c']
        rotor.rotate(list, 1)
        self.assertEquals(['c','a','b'], list)

    def test_get_letter_position_method(self):
        rotor = Rotor(1, 'A')
        position = rotor.get_letter_position_in_alphabet('a')
        self.assertEquals(1, position)
        position = rotor.get_letter_position_in_alphabet('h')
        self.assertEquals(8, position)
        position = rotor.get_letter_position_in_alphabet('Z')
        self.assertEquals(26, position)

    def test_get_letter_from_alphabet_method(self):
        rotor = Rotor(1, 'A')
        position = rotor.get_letter_from_alphabet(1)
        self.assertEquals('A', position)
        position = rotor.get_letter_from_alphabet(8)
        self.assertEquals('H', position)
        position = rotor.get_letter_from_alphabet(26)
        self.assertEquals('Z', position)