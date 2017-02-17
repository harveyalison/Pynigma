from Pynigma.enums import ReflectorType

class Reflector:
    """Object representing a physical Enigma reflector
    """

    def __init__(self, reflector_type = None):
        self.connections = []

        # As the reflector was normally fixed (not specified in the key)
        # it makes sense to allow a default value
        if reflector_type == None:
            reflector_type = ReflectorType.B

        self.reflector_type = reflector_type

        # The reflectors available to the operator had different internal wiring connections
        # Source: http://www.codesandciphers.org.uk/enigma/rotorspec.htm
        if self.reflector_type == ReflectorType.B:
            self.connections = ['AY','BR','CU','DH','EQ','FS','GL','IP','JX','KN','MO','TZ','VW']
        elif self.reflector_type == ReflectorType.C:
            self.connections = ['AF','BV','CP','DJ','EI','GO','HY','KR','LZ','MX','NW','TQ','SU']
        elif self.reflector_type == ReflectorType.B_Dunn:
            self.connections = ['AE','BN','CK','DQ','FU','GY','HW','IJ','LO','MP','RX','SZ','TV']
        elif self.reflector_type == ReflectorType.C_Dunn:
            self.connections = ['AR','BD','CO','EJ','FN','GT','HK','IV','LM','PW','QZ','SX','UY']

    def get_reflection(self, letter):
        """Returns the output letter of the reflector for the given input"""
        for pair in self.connections:
            if letter in pair:
                return pair.replace(letter,'')