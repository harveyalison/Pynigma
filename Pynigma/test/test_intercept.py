import unittest

import datetime

from Pynigma.intercept import Intercept


class InterceptTests(unittest.TestCase):

    def test_intercept_instantiation(self):
        intercept = Intercept()

    def test_intercept_default_member_values(self):
        intercept = Intercept()
        self.assertEquals(intercept.frequency_kHz, 0)
        self.assertEquals(intercept.time_of_intercept, datetime.MINYEAR)

    def test_intercept_instantiate_member_values(self):
        intercept = Intercept(datetime.MAXYEAR, 123)
        self.assertEquals(intercept.frequency_kHz, 123)
        self.assertEquals(intercept.time_of_intercept, datetime.MAXYEAR)