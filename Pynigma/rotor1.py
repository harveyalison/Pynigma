from Pynigma.rotor import Rotor


class Rotor1(Rotor):

    def __init__(self):
        self.connections = {
            'A' : 'E',
            'B' : 'K',
            'C' : 'M',
            'D' : 'F',
            'E' : 'L',
            'F' : 'G',
            'G' : 'D',
            'H' : 'Q',
            'I' : 'V',
            'J' : 'Z',
            'K' : 'N',
            'L' : 'T',
            'M' : 'O',
            'N' : 'W',
            'O' : 'Y',
            'P' : 'H',
            'Q' : 'X',
            'R' : 'U',
            'S' : 'S',
            'T' : 'P',
            'U' : 'A',
            'V' : 'I',
            'W' : 'B',
            'X' : 'R',
            'Y' : 'C',
            'Z' : 'J'
        }