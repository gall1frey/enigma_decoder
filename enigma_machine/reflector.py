'''
Author: Gallifrey (github.com/gall1frey)
Class Reflector for Enigma
This class simulates the reflector in an enigma
machine. The Enigma class depends
on this.
'''

class Reflector:
    '''
        Class Reflector for Enigma Machine
    '''
    def __init__(self,name):
        '''
            Constructor for class Reflector
            Input: Name (Type) of constructor.
                    Can be 'A', 'B', or 'C'
            Sets the encoding (obtained from wikipedia)
            and wiring
        '''
        if name == 'C':
            self.encoding = 'FVPJIAOYEDRZXWGCTKUQSBNMHL'
        elif name == 'B':
            self.encoding = 'YRUHQSLDPXNGOKMIEBFZCWVJAT'
        else:
            self.encoding = 'EJMZALYXVBWFCRQUONTSPIKHGD'
        self.wiring = self.get_wiring()

    def get_wiring(self):
        '''
            Returns entire list of wiring
        '''
        return list(ord(i)-65 for i in self.encoding)

    def forward(self,char_code):
        '''
            Enciphers using the reflector wiring
        '''
        return self.wiring[char_code]
