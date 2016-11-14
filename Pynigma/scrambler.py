from Pynigma import preamble

class Scrambler:
    """Object representing the scrambler unit of an Enigma.
    The military version of the Enigma machine had five wheels,
    three of which could be fitted in the scrambler at any time.
    The input signal first went through a 'Commutator' (C),
    a fixed shallow cylinder containing 26 terminals, corresponding
    to the letters of the alphabet. The signal then went in turn
    through 3 movable wheels, through a fixed 'turn-around' cylinder,
    or 'umkehrwalze' (U), and back out again, as shown.

    U    3    2    1    C
    --  ---  ---  ---  --
    | -> | -> | -> | -> | -> Signal out
    |    |    |    |    |
    |    |    |    |    |
    | <- | <- | <- | <- | <- Signal in
    --  ---  ---  ---  --

    After each letter was scrambled, wheel 1 was rotated a single
    step. One of the steps in each wheel causes the wheel to its'
    left to rotate a step i.e. for every 26 steps of the wheel in
    position 1, the wheel in position 2 moves on a step, and for
    every 26 steps of the wheel in position 2, the wheel in position
    3 moves on a step.
    """

    def scramble(self, letter):
        """Encipher the message"""
        cipher_text = 'lalala'

        pre = preamble.get_preamble()

        return pre + \
               'Plain text: ' + message + '\r\n' \
               'Cipher text: ' + cipher_text

