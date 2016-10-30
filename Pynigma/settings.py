import datetime

"""Unenciphered Enigma message preamble
"""

#Call signs of the statins involved. First the sending station, then the destination(s)
CALL_SIGNS = {'P7J', 'SF9', '5KQ'}

#Date and Time of the origin of the message
DATE_OF_ORIGIN = datetime.datetime.now().date()
TIME_OF_ORIGIN = datetime.datetime.now().time()

NUMBER_OF_LETTERS = 0

# An indication of whether the message is complete,
# or part of a larger message e.g. {2,4} would indicate
# part 2 of a 4 part message
SINGLE_OR_MULTIPART = {1,1}

# A three letter group to distinguish between different
# types of Enigma traffic
DISCRIMINANT = 'ABC'

# A three letter group, relating to the encoding of the message
INDICATOR_SETTING = 'DEF'


