class Rotor:
    """Base object representing a physical Enigma rotor (or wheel)

    A rotor:

    1: is movable, and has 26 positions, corresponding to the letters of the alphabet.
    2: has a fixed commutator, with 26 connections.
    3: has a movable ring, which associates a letter of the alphabet with a commutator position.
    4: has a single position which it causes a rotor to its left to be advanced, when it is advanced itself.

    The combination of the commutator and the ring position fixes the input of the rotor
    relative to the output.



    """

    connections = {}
    current_position = 0
    ring_position = 0
    stepping_position = 0

    def __init__(self, rotor_number):
        if rotor_number == 1:
            self.connections = self.ROTOR_1_CONNECTIONS
        elif rotor_number == 2:
            self.connections = self.ROTOR_2_CONNECTIONS
        elif rotor_number == 3:
            self.connections = self.ROTOR_3_CONNECTIONS
        elif rotor_number == 4:
            self.connections = self.ROTOR_4_CONNECTIONS
        elif rotor_number == 5:
            self.connections = self.ROTOR_5_CONNECTIONS

    def advance(self):
        """Move the rotor to the next position"""
        pass

    def get_connection(self, letter):
        return self.connections[str(letter).upper()]


    ROTOR_1_CONNECTIONS = {
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

    ROTOR_2_CONNECTIONS = {
            'A' : 'A',
            'B' : 'J',
            'C' : 'D',
            'D' : 'K',
            'E' : 'S',
            'F' : 'I',
            'G' : 'R',
            'H' : 'U',
            'I' : 'X',
            'J' : 'B',
            'K' : 'L',
            'L' : 'H',
            'M' : 'W',
            'N' : 'T',
            'O' : 'M',
            'P' : 'C',
            'Q' : 'Q',
            'R' : 'G',
            'S' : 'Z',
            'T' : 'N',
            'U' : 'P',
            'V' : 'Y',
            'W' : 'F',
            'X' : 'V',
            'Y' : 'O',
            'Z' : 'E'
        }

    ROTOR_3_CONNECTIONS = {
            'A' : 'B',
            'B' : 'D',
            'C' : 'F',
            'D' : 'H',
            'E' : 'J',
            'F' : 'L',
            'G' : 'C',
            'H' : 'P',
            'I' : 'R',
            'J' : 'T',
            'K' : 'X',
            'L' : 'V',
            'M' : 'Z',
            'N' : 'N',
            'O' : 'Y',
            'P' : 'E',
            'Q' : 'I',
            'R' : 'W',
            'S' : 'G',
            'T' : 'A',
            'U' : 'K',
            'V' : 'M',
            'W' : 'U',
            'X' : 'S',
            'Y' : 'Q',
            'Z' : 'O'
        }

    ROTOR_4_CONNECTIONS = {
            'A' : 'E',
            'B' : 'S',
            'C' : 'O',
            'D' : 'V',
            'E' : 'P',
            'F' : 'Z',
            'G' : 'J',
            'H' : 'A',
            'I' : 'Y',
            'J' : 'Q',
            'K' : 'U',
            'L' : 'I',
            'M' : 'R',
            'N' : 'H',
            'O' : 'X',
            'P' : 'L',
            'Q' : 'N',
            'R' : 'F',
            'S' : 'T',
            'T' : 'G',
            'U' : 'K',
            'V' : 'D',
            'W' : 'C',
            'X' : 'M',
            'Y' : 'W',
            'Z' : 'B'
        }

    ROTOR_5_CONNECTIONS = {
            'A' : 'V',
            'B' : 'Z',
            'C' : 'B',
            'D' : 'R',
            'E' : 'G',
            'F' : 'I',
            'G' : 'T',
            'H' : 'Y',
            'I' : 'U',
            'J' : 'P',
            'K' : 'S',
            'L' : 'D',
            'M' : 'N',
            'N' : 'H',
            'O' : 'L',
            'P' : 'X',
            'Q' : 'A',
            'R' : 'W',
            'S' : 'M',
            'T' : 'J',
            'U' : 'Q',
            'V' : 'O',
            'W' : 'F',
            'X' : 'E',
            'Y' : 'C',
            'Z' : 'K'
        }

    #Rotor VI	J	P	G	V	O	U	M	F	Y	Q	B	E	N	H	Z	R	D	K	A	S	X	L	I	C	T	W
    #Rotor VII	N	Z	J	H	G	R	C	X	M	Y	S	W	B	O	U	F	A	I	V	L	P	E	K	Q	D	T
    #Rotor VIII	F	K	Q	H	T	L	X	O	C	B	J	S	P	D	Z	R	A	M	E	W	N	I	U	Y	G	V
    #Beta rotor	L	E	Y	J	V	C	N	I	X	W	P	B	Q	M	D	R	T	A	K	Z	G	F	U	H	O	S
    #Gamma rotor	F	S	O	K	A	N	U	E	R	H	M	B	T	I	Y	C	W	L	Q	P	Z	X	V	G	J	D