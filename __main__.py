import argparse
from Pynigma import preamble
from Pynigma.enigma import Enigma

parser = argparse.ArgumentParser(description='Encode or decode a message using Enigma')

parser.add_argument('message', help='message to encipher / decipher', nargs='?', default='Hut 6')

#TODO: add support to optionally read message from a file
#input_group = parser.add_mutually_exclusive_group()
#input_group.add_argument('-m', '--message', type=str, help='message to encipher / decipher', default='Hut 6')
#input_group.add_argument('-if', '--input_file', type=str, help='file containing the message to encipher / decipher')

#TODO: add support to write the output to a file
#output_group = parser.add_mutually_exclusive_group()
#output_group.add_argument('-o', '--output', action='store_true', help='output the enciphered / deciphered message to std out')
#output_group.add_argument('-of', '--output_file', type=str, help='output the enciphered / deciphered message to file')

parser.add_argument('-dsc', '--discriminant', \
                    type=str, \
                    help='three letter group, used to distinguish between different types of Enigma traffic', \
                    default='ABC')
parser.add_argument('-ind', '--indicator', \
                    type=str, \
                    help='three letter group, used in encoding and decoding the message', \
                    default='DEF')
parser.add_argument('-d', '--double_encipher', action='store_true',  \
                    help='double enciphering of the indicator setting, as used until May 10 1940.' \
                    ' If not specified, will use single encihering of the indicator setting, \
                    as used after May 10 1940.')

#endregion

args = parser.parse_args()

#TODO: validate args

#region un-comment to debug args
#print('Settings used...')
#print('Message: ' + args.message)
#print('Discriminant: ' + args.discriminant)
#print('Indicator setting: ' + args.indicator)
#if args.double_encipher:
#    print('Double encipher indicator setting')
#else:
#    print('Single encipher indicator setting')
#endregion

preamble.DISCRIMINANT = args.discriminant
preamble.INDICATOR_SETTING = args.indicator

e = Enigma()

print(e.encipher(args.message))