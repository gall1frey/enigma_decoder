'''
Author: Gallifrey (github.com/gall1frey)
Class Reflector for Enigma
'''

class Reflector:
    def __init__(self,name):
        if name == 'C':
            self.encoding = 'FVPJIAOYEDRZXWGCTKUQSBNMHL'
        elif name == 'B':
            self.encoding = 'YRUHQSLDPXNGOKMIEBFZCWVJAT'
        else:
            self.encoding = 'EJMZALYXVBWFCRQUONTSPIKHGD'
        self.wiring = self.get_wiring()

    def get_wiring(self):
        wiring = list(ord(i)-65 for i in self.encoding)
        return wiring

    def forward(self,char_code):
        return self.wiring[char_code]
