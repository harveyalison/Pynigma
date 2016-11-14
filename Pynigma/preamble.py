import datetime

"""Unenciphered Enigma message preamble
"""

#Call signs of the statins involved. First the sending station, then the destination(s)
#e.g. 'From P7J to SF9 and 5KQ'
CALL_SIGNS = 'Not yet implemented'

#Date and Time of the origin of the message
DATE_OF_ORIGIN = datetime.datetime.now().date()
TIME_OF_ORIGIN = datetime.datetime.now().time()

NUMBER_OF_LETTERS = 0

# An indication of whether the message is complete,
# or part of a larger message e.g. 'Part 2 of a 4 part message'
SINGLE_OR_MULTIPART = 'Not yet implemented'

# A three letter group to distinguish between different
# types of Enigma traffic
DISCRIMINANT = 'ABC'

# A three letter group, relating to the encoding of the message
INDICATOR_SETTING = 'DEF'


def get_preamble():
    return \
        'Call signs: ' + str(CALL_SIGNS) + '\r\n' + \
        'Date of origin: ' + str(DATE_OF_ORIGIN) + '\r\n' + \
        'Time of origin: ' + str(TIME_OF_ORIGIN) + '\r\n' + \
        'Number of letters: ' + str(NUMBER_OF_LETTERS) + '\r\n' + \
        'Single or multi-part: ' + str(SINGLE_OR_MULTIPART) + '\r\n' + \
        'Discriminant: ' + str(DISCRIMINANT) + '\r\n' + \
        'Indicator setting: ' + str(INDICATOR_SETTING) + '\r\n'