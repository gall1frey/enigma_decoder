'''
Author: Gallifrey (github.com/gall1frey)
Class Rotor for Enigma
This class simulates a rotor in an enigma
machine. The Enigma class depends
on this.
'''

class Rotor:
    '''
        Rotor class for Enigma Machine
    '''
    def __init__(self,):
        '''
            Constructor for Rotor class
        '''
        self.name = None
        self.encoding = None
        self.rotorPosition = None
        self.notchPosition = None
        self.ringSetting = None
        self.forward_wiring = None
        self.backwardWiring = None

    def get_name(self):
        '''
            Utility function to get name of the rotor
            Returns name of the rotor
        '''
        return self.name

    def get_position(self):
        '''
            Utility function to get position of the rotor
            Returns position of the rotor
        '''
        return self.rotorPosition

    def create_rotor(self,name,rotorPosition,ringSetting):
        '''
            Creates a rotor. i.e. Initializes the name,
            rotor position, ring settings and wirings
        '''
        if name == "I":
            self.name = "I"
            self.encoding = "EKMFLGDQVZNTOWYHXUSPAIBRCJ"
            self.rotorPosition = rotorPosition
            self.notchPosition = 14
            self.ringSetting = ringSetting
        elif name == "II":
            self.name = "II"
            self.encoding = "AJDKSIRUXBLHWTMCQGZNPYFVOE"
            self.notchPosition = 4
            self.rotorPosition = rotorPosition
            self.ringSetting = ringSetting
        elif name == "III":
            self.name = "III"
            self.encoding = "BDFHJLCPRTXVZNYEIWGAKMUSQO"
            self.notchPosition = 21
            self.rotorPosition = rotorPosition
            self.ringSetting = ringSetting
        elif name == "IV":
            self.name = "IV"
            self.encoding = "ESOVPZJAYQUIRHXLNFTGKDCMWB"
            self.notchPosition = 9
            self.rotorPosition = rotorPosition
            self.ringSetting = ringSetting
        elif name == "V":
            self.name = "V"
            self.encoding = "VZBRGITYUPSDNHLXAWMJQOFECK"
            self.notchPosition = 25
            self.rotorPosition = rotorPosition
            self.ringSetting = ringSetting
        elif name == "VI":
            self.name = "VI"
            self.encoding = "JPGVOUMFYQBENHZRDKASXLICTW"
            self.notchPosition = 0
            self.rotorPosition = rotorPosition
            self.ringSetting = ringSetting
        elif name == "VII":
            self.name = "VII"
            self.encoding = "NZJHGRCXMYSWBOUFAIVLPEKQDT"
            self.notchPosition = 0
            self.rotorPosition = rotorPosition
            self.ringSetting = ringSetting
        elif name == "VIII":
            self.name = "VIII"
            self.encoding = "FKQHTLXOCBJSPDZRAMEWNIUYGV"
            self.notchPosition = 0
            self.rotorPosition = rotorPosition
            self.ringSetting = ringSetting
        else:
            self.name = "Identity"
            self.encoding = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            self.notchPosition = 0
            self.rotorPosition = rotorPosition
            self.ringSetting = ringSetting
        if self.name != 'Identity':
            self.set_forward_wiring()
            self.set_backward_wiring()

    def is_at_notch(self):
        '''
            Returns True if the rotor is at notch position
        '''
        if self.name in ['VI','VII','VIII']:
            return self.rotorPosition == 12 or self.rotorPosition == 25;
        return self.notchPosition == self.rotorPosition;

    def turnover(self):
        '''
            Effectively rotates the rotor one position
        '''
        self.rotorPosition = (self.rotorPosition + 1) % 26

    def set_forward_wiring(self):
        '''
            Set forward wiring
            (For when going right to left)
        '''
        self.forward_wiring = list(ord(i)-65 for i in self.encoding)

    def set_backward_wiring(self):
        '''
            Set backward wiring
            (For when going left to right)
        '''
        self.backward_wiring = list(ord(i)-65 for i in self.encoding)
        for i in range(len(self.forward_wiring)):
            forward = self.forward_wiring[i]
            self.backward_wiring[forward] = i

    def encipher(self,char_code,mapping):
        '''
            Returns number enciphered by one rotor
            Input: character (int),
                mapping (forward/backward wiring) (int list)
            Output: character (int)
        '''
        rotor_pos, ring = self.rotorPosition, self.ringSetting
        shift = rotor_pos - ring
        return (mapping[(char_code + shift + 26) % 26] - shift + 26) % 26

    def forward(self,char_code):
        '''
            Encipher going right to left
        '''
        return self.encipher(char_code, self.forward_wiring)

    def backward(self,char_code):
        '''
            Encipher going left to right
        '''
        return self.encipher(char_code, self.backward_wiring)
