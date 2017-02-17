import unittest
from Pynigma.reflector import Reflector
from Pynigma.enums import ReflectorType

class ReflectorTests(unittest.TestCase):

    def test_reflector_instantiation(self):
        reflector = Reflector(ReflectorType.B)

    def test_reflector_B_reflections(self):
        reflector = Reflector(ReflectorType.B)
        a_reflection = reflector.get_reflection('A')
        b_reflection = reflector.get_reflection('B')
        c_reflection = reflector.get_reflection('C')

        self.assertEquals('Y', a_reflection)
        self.assertEquals('R', b_reflection)
        self.assertEquals('U', c_reflection)

    def test_reflector_C_Dünn_reflections(self):
        reflector = Reflector(ReflectorType.C_Dunn)
        a_reflection = reflector.get_reflection('A')
        r_reflection = reflector.get_reflection('R')
        s_reflection = reflector.get_reflection('S')
        e_reflection = reflector.get_reflection('E')

        self.assertEquals('R', a_reflection)
        self.assertEquals('A', r_reflection)
        self.assertEquals('X', s_reflection)
        self.assertEquals('J', e_reflection)
