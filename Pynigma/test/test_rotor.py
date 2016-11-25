import unittest
from Pynigma.rotor import Rotor

class RotorTests(unittest.TestCase):

    def test_rotor_instantiation(self):
        rotor = Rotor(1,'A')

    def test_rotor_1_values(self):
        rotor = Rotor(1,'A')
        a_connection = rotor.get_connection('A')
        b_connection = rotor.get_connection('B')
        c_connection = rotor.get_connection('C')

        self.assertEquals('E', a_connection)
        self.assertEquals('K', b_connection)
        self.assertEquals('M', c_connection)

    def test_rotor_1_values_with_ring_setting(self):
        rotor = Rotor(1,'B')
        a_connection = rotor.get_connection('A')
        b_connection = rotor.get_connection('B')
        c_connection = rotor.get_connection('C')

        self.assertEquals('K', a_connection)
        self.assertEquals('M', b_connection)
        self.assertEquals('F', c_connection)

        rotor = Rotor(1, 'F')
        a_connection = rotor.get_connection('A')
        b_connection = rotor.get_connection('B')
        c_connection = rotor.get_connection('C')

        self.assertEquals('G', a_connection)
        self.assertEquals('D', b_connection)
        self.assertEquals('Q', c_connection)

        rotor = Rotor(1, 'Z')
        a_connection = rotor.get_connection('A')
        b_connection = rotor.get_connection('B')
        c_connection = rotor.get_connection('C')

        self.assertEquals('J', a_connection)
        self.assertEquals('E', b_connection)
        self.assertEquals('K', c_connection)

    def test_rotor_1_values_with_ring_setting2(self):
        rotor = Rotor(1, 'C')
        a_connection = rotor.get_connection('A')
        b_connection = rotor.get_connection('B')
        c_connection = rotor.get_connection('C')

        self.assertEquals('M', a_connection)
        self.assertEquals('F', b_connection)
        self.assertEquals('L', c_connection)


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