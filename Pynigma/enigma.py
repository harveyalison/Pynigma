from Pynigma import preamble

class Enigma:
    """Object representing an Enigma

    """

    def encipher(self, message):
        """Encipher the message"""
        cipher_text = 'lalala'

        pre = preamble.get_preamble()

        return pre + cipher_text

