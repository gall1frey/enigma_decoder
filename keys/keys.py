'''
    class enigmaKey
    Basically a fancy container to store
    the settings of an enigma machine
'''
class enigmaKey:
    def __init__(self,rotors,pos,reflector,ring_settings,plugboard,score):
        self.rotors = rotors
        self.pos = pos
        self.reflector = reflector
        self.ring_settings = ring_settings
        self.plugboard = plugboard
        self.score = score
