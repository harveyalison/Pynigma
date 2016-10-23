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

    def advance(self):
        """Move the rotor to the next position"""
        pass
