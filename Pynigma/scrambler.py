from Pynigma.rotor import Rotor

class Scrambler:
    """Object representing the scrambler unit of an Enigma.
    The military version of the Enigma machine had five rotors,
    three of which could be fitted in the scrambler at any time.
    The input signal first went through a 'Commutator' (C),
    a fixed shallow cylinder containing 26 terminals, corresponding
    to the letters of the alphabet. The signal then went in turn
    through 3 movable rotors, through a fixed 'turn-around' cylinder,
    or 'umkehrwalze' (U), and back out again, as shown.

    U    3    2    1    C
    --  ---  ---  ---  --
    | -> | -> | -> | -> | -> Signal out
    |    |    |    |    |
    |    |    |    |    |
    | <- | <- | <- | <- | <- Signal in
    --  ---  ---  ---  --

    After each letter was scrambled, rotor 1 was advanced a single
    step. One of the steps in each rotor causes the rotor to its'
    left to advance a step i.e. for every 26 steps of the rotor in
    position 1, the rotor in position 2 moves on a step, and for
    every 26 steps of the rotor in position 2, the rotor in position
    3 moves on a step.
    """

    def __init__(self, rotor_order):
        print('rotor order = ' + rotor_order)
        self.rotor1 = Rotor(int(rotor_order[0]))
        self.rotor2 = Rotor(int(rotor_order[1]))
        self.rotor3 = Rotor(int(rotor_order[2]))

    def scramble(self, letter):
        """Encipher the letter"""
        cipher_letter = self.rotor1.get_connection(letter)
        cipher_letter = self.rotor2.get_connection(letter)
        cipher_letter = self.rotor3.get_connection(letter)

        #TODO: implement reflector and call it here

        cipher_letter = self.rotor3.get_connection(letter)
        cipher_letter = self.rotor2.get_connection(letter)
        cipher_letter = self.rotor1.get_connection(letter)

        return 'x' #cipher_letter