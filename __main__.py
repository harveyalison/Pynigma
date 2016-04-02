import argparse

parser = argparse.ArgumentParser(description="Encode or decode a message using Enigma")
operation_group = parser.add_mutually_exclusive_group()
operation_group.add_argument("-ee", "--double_encipher", action="store_true", help="As used until May 10 1940")
operation_group.add_argument("-e", "--single_encipher", action="store_true", help="As used after May 10 1940")
operation_group.add_argument("-dd", "--double_decipher", action="store_true", help="As used until May 10 1940")
operation_group.add_argument("-d", "--single_decipher", action="store_true", help="As used after May 10 1940")
parser.add_argument("-dsc", "--discriminant", type=str, \
                    help="A three letter group, used to distinguish between different types of Enigma traffic")
parser.add_argument("-ind", "--indicator", type=str, \
                    help="A three letter group, used in encoding and decoding the message")

input_group = parser.add_mutually_exclusive_group()
input_group.add_argument("-i", "--input", type=str, help="The message to encipher / decipher")
input_group.add_argument("-if", "--input_file", type=str, help="The file containing the message to encipher / decipher")

output_group = parser.add_mutually_exclusive_group()
output_group.add_argument("-o", "--output", action="store_true", help="Output the enciphered / deciphered message to std out")
output_group.add_argument("-of", "--output_file", type=str, help="Output the enciphered / deciphered message to file")

args = parser.parse_args()

if args.e:
    print("TODO: Single encipher")
elif args.ee:
    print("TODO: Double encipher")