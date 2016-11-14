import json
from Pynigma.settings import *

class KeyReader:
    """Docs
    """

    def __init__(self, key_file_name):
        #TODO: validate file exists, is valid JSON etc.
        with open(key_file_name) as data_file:
            self.keys = json.load(data_file)

    def get_rotor_order(self, date):
        try:
            rotor_order = self.keys[date]['rotor_order']
        except KeyError:
            rotor_order = DEFAULT_ROTOR_ORDER
        return rotor_order

    def get_ring_settings(self, date):
        try:
            ring_settings = self.keys[date]['ring_settings']
        except KeyError:
            ring_settings = DEFAULT_RING_SETTINGS
        return ring_settings

    def get_cross_pluggings(self, date):
        try:
            cross_pluggings = self.keys[date]['cross_pluggings']
        except KeyError:
            cross_pluggings = DEFAULT_CROSS_PLUGGINGS
        return cross_pluggings