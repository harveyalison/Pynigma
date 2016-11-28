import unittest

from Pynigma.key_reader import *

class KeyReaderTests(unittest.TestCase):

    def test_key_reader_instantiation(self):
        key_reader = KeyReader('../keys.txt')

    def test_key_reader_for_valid_date(self):
        key_reader = KeyReader('../keys.txt')
        cross_pluggings = key_reader.get_cross_pluggings('2016-11-20')
        ring_settings = key_reader.get_ring_settings('2016-11-20')
        rotor_order = key_reader.get_rotor_order('2016-11-20')

        self.assertEquals(cross_pluggings, 'KY,TO,ZL,BU,WD,CX,IJ,GA,PH,NR,FM')
        self.assertEquals(ring_settings, 'DOH')
        self.assertEquals(rotor_order, '413')

    def test_key_reader_for_invalid_date(self):
        key_reader = KeyReader('../keys.txt')
        cross_pluggings = key_reader.get_cross_pluggings('1939-01-01')
        ring_settings = key_reader.get_ring_settings('1939-01-01')
        rotor_order = key_reader.get_rotor_order('1939-01-01')

        #Should be using defaults, defined in settings.py
        self.assertEquals(cross_pluggings, 'TO,KY,ZL,BU,WD,CX,IJ,GA,PH,NR,FM')
        self.assertEquals(ring_settings, 'HGA')
        self.assertEquals(rotor_order, '421')