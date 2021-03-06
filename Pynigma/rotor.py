class Rotor:
    """Object representing a physical Enigma rotor (or wheel)

    A rotor:

    1: is movable, and has 26 positions, corresponding to the letters of the alphabet.
    2: has a fixed commutator, with 26 connections.
    3: has a movable ring, which associates a letter of the alphabet with a commutator position.
    4: has a single position which it causes a rotor to its left to be advanced, when it is advanced itself.

    The combination of the commutator and the ring position fixes the input of the rotor
    relative to the output.

    """

    def __init__(self, rotor_id, ring_setting):
        self.connections = []
        self.rotor_id = rotor_id

        # The rotors available to the operator had different internal wiring connections
        # Source: http://www.codesandciphers.org.uk/enigma/rotorspec.htm
                               #'A' 'B' 'C' 'D' 'E' 'F' 'G' 'H' 'I' 'J' 'K' 'L' 'M' 'N' 'O' 'P' 'Q' 'R' 'S' 'T' 'U' 'V' 'W' 'X' 'Y' 'Z'
        if self.rotor_id == 1:
            self.connections = ['E','K','M','F','L','G','D','Q','V','Z','N','T','O','W','Y','H','X','U','S','P','A','I','B','R','C','J']
        elif self.rotor_id == 2:
            self.connections = ['A','J','D','K','S','I','R','U','X','B','L','H','W','T','M','C','Q','G','Z','N','P','Y','F','V','O','E']
        elif self.rotor_id == 3:
            self.connections = ['B','D','F','H','J','L','C','P','R','T','X','V','Z','N','Y','E','I','W','G','A','K','M','U','S','Q','O']
        elif self.rotor_id == 4:
            self.connections = ['E','S','O','V','P','Z','J','A','Y','Q','U','I','R','H','X','L','N','F','T','G','K','D','C','M','W','B']
        elif self.rotor_id == 5:
            self.connections = ['V','Z','B','R','G','I','T','Y','U','P','S','D','N','H','L','X','A','W','M','J','Q','O','F','E','C','K']
        elif self.rotor_id == 6:
            self.connections = ['J','P','G','V','O','U','M','F','Y','Q','B','E','N','H','Z','R','D','K','A','S','X','L','I','C','T','W']
        elif self.rotor_id == 7:
            self.connections = ['N','Z','J','H','G','R','C','X','M','Y','S','W','B','O','U','F','A','I','V','L','P','E','K','Q','D','T']
        elif self.rotor_id == 8:
            self.connections = ['F','K','Q','H','T','L','X','O','C','B','J','S','P','D','Z','R','A','M','E','W','N','I','U','Y','G','V']
        elif self.rotor_id == 'Beta':
            self.connections = ['L','E','Y','J','V','C','N','I','X','W','P','B','Q','M','D','R','T','A','K','Z','G','F','U','H','O','S']
        elif self.rotor_id == 'Gamma':
            self.connections = ['F','S','O','K','A','N','U','E','R','H','M','B','T','I','Y','C','W','L','Q','P','Z','X','V','G','J','D']

        # The wiring in a rotor could be rotated to begin at a different letter, given in the daily key
        self.position = self.get_letter_position_in_alphabet(ring_setting) - 1
        self.rotate(self.connections, -self.position)

    def at_step_position(self):
        #TODO: work out whether the rotor indicator is at the step position
        #Rotor I at R
        #Rotor II at F
        #Rotor III at W
        #Rotor IV at K
        #Rotor V at A
        #Rotors VI, VII and VIII at A and at N

        #if self.rotor_id == 1:
        #elif self.rotor_id == 2:
        #elif self.rotor_id == 3:
        #elif self.rotor_id == 4:
        #elif self.rotor_id == 5:
        #elif self.rotor_id == 6:
        #elif self.rotor_id == 7:
        #elif self.rotor_id == 8:
        #elif self.rotor_id == 'Beta':
        #elif self.rotor_id == 'Gamma':
        pass

    def advance(self):
        """Move the rotor to the next position"""
        self.rotate(self.connections, -1)

    def get_output(self, letter):
        """Returns the output letter of the rotor for the given input"""
        position = self.get_letter_position_in_alphabet(letter)
        return self.connections[position - 1]

    def get_input(self, letter):
        """Returns the input letter of the rotor for the given output"""
        index = self.connections.index(letter)
        return self.get_letter_from_alphabet(index + 1)

    def get_letter_position_in_alphabet(self, letter):
        """Returns the position of the supplied letter in the alphabet
        e.g. A returns 1, Z returns 26"""
        alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        return alphabet.index(str(letter).upper()) +1

    def get_letter_from_alphabet(self, position):
        """Returns the letter of the alphabet with the supplied
        numerical position e.g. 1 returns 'A', 26 returns 'Z'"""
        alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        return alphabet[position - 1]

    def rotate(self, lst, x):
        lst[:] = lst[-x:] + lst[:-x]