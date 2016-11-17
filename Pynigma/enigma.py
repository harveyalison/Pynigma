import string

from Pynigma import preamble
from Pynigma.key_reader import KeyReader
from Pynigma.scrambler import Scrambler
import datetime
import os
import sys

class Enigma:
    """Object representing an Enigma

    """

    def __init__(self):
        #region Get the keys
        dir = os.path.dirname(__file__)
        keys_file = os.path.join(dir, 'keys.txt')
        self.keys = KeyReader(keys_file)
        #endregion

        #region Get today's rotor order
        date_as_string = datetime.datetime.now().date().strftime('%Y-%m-%d')
        self.rotor_order = self.keys.get_rotor_order(date_as_string)
        #endregion

        #Initialise the scrambler
        self.scrambler = Scrambler(self.rotor_order)

    def encipher(self, message):
        """Encipher the message"""

        # region Enigma could not encipher spaces or punctuation or numbers

        if (sys.version_info > (3, 0)):
            # Python 3 code in this block
            table = str.maketrans({key: None for key in string.punctuation})
            message_no_punctuation = message.translate(table)
        else:
            # Python 2 code in this block
            table = string.maketrans("", "")
            message_no_punctuation = message.translate(table, string.punctuation)

        message_no_spaces_or_punctuation = message_no_punctuation.replace(" ", "")
        message_no_spaces_or_punctuation_or_numbers = ''.join(
            [i for i in message_no_spaces_or_punctuation if not i.isdigit()])

        # endregion

        cipher_text = ''

        pre = preamble.get_preamble()

        for letter in message_no_spaces_or_punctuation_or_numbers:
            cipher_text += self.scrambler.scramble(letter)

        return pre + \
               'Plain text: ' + message + '\r\n' \
               'Cipher text: ' + cipher_text

