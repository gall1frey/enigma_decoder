'''
Author: Gallifrey (github.com/gall1frey)
Class Enigma
This class brings together the Rotor,
Plugboard and Reflector classes to make
the enigma machine
'''
from rotor import Rotor
from plugboard import Plugboard
from reflector import Reflector


class Enigma:
    '''
        Class Enigma, the working enigma machine
        Classes Used: Rotor, Plugboard, Reflector
        Class Methods: __init__, set_rotors, rotate,
            only_alpha, to_num_list, encrypt_int,
            from_num_list, encrypt, set_plugboard
    '''

    def __init__(self,rotors='I II III',reflector='',rotor_positions=[0,0,0],ring_settings=[0,0,0],plugboard_connections=[]):
        '''
            Constructor for class Enigma.
            Args: rotors -> space separated string
                    with rotors used as roman numerals.
                    Eg: I II IV
                  reflector -> Reflector used. Char.
                    Can be A, B or C
                  rotor_positions -> Rotor positions
                    Int list
                  ring settings -> Ring Settings
                    Int list
                  plugboard_connections -> Connections made on the plugboard_connections
                    list of tuples
        '''
        self.rotors = rotors.split(' ')

        #Creating objects of the Rotor class for the left, middle and right rotors
        self.rotor_left = Rotor()
        self.rotor_middle = Rotor()
        self.rotor_right = Rotor()
        #set parameters of the rotors
        self.set_rotors(rotor_positions,ring_settings)

        #Creating an object of the Plugboard class for the plugboard
        self.plugboard = Plugboard()
        #Set the plugboard
        self.set_plugboard(plugboard_connections)

        #Creating an object of the Reflector class for the reflector
        self.reflector = Reflector(reflector)

    def set_rotors(self,rotor_positions,ring_settings):
        '''
            Sets rotor configurations.
            Args: rotor_positions [int list], ring_settings [int list]
            Returns: None
        '''
        self.rotor_left.create_rotor(self.rotors[0],rotor_positions[0],ring_settings[0])
        self.rotor_middle.create_rotor(self.rotors[1],rotor_positions[1],ring_settings[1])
        self.rotor_right.create_rotor(self.rotors[2],rotor_positions[2],ring_settings[2])

    def rotate(self):
        '''
            Handles rotating of the rotors
        '''
        if self.rotor_middle.is_at_notch():
            self.rotor_middle.turnover()
            self.rotor_left.turnover()
        elif self.rotor_right.is_at_notch():
            self.rotor_middle.turnover()
        self.rotor_right.turnover();

    def only_alpha(self,in_str):
        '''
            Drops any non alphabetic character in input string
            Converts all to uppercase
            Input: String to encrypt
            Output: Better formatted string to encrypt
        '''
        return ''.join(char for char in in_str if char.isalpha()).upper()

    def to_num_list(self,in_str):
        '''
            Converts string to list of numbers
            A -> 0 | B -> 1 | C -> 2 | etc.
            Input: String
            Output: List of numbers
        '''
        return list(ord(i)-65 for i in in_str)

    def from_num_list(self,num_list):
        '''
            Converts a list of numbers to string
            (Inverse of to_num_list)
            Input: List of numbers
            Output: String
        '''
        return ''.join(chr(i+65) for i in num_list)

    def encrypt_int(self,in_int):
        '''
            Encrypts an integer
            Input: Integer to encrypt
            Output: Encrypted Integer
        '''
        self.rotate();
        #Plugboard
        in_int = self.plugboard.get_plugboard_output(in_int)
        #To the reflector
        c1 = self.rotor_right.forward(in_int)
        c2 = self.rotor_middle.forward(c1)
        c3 = self.rotor_left.forward(c2)
        #At the reflector
        c4 = self.reflector.forward(c3)
        #From the reflector
        c5 = self.rotor_left.backward(c4)
        c6 = self.rotor_middle.backward(c5)
        c7 = self.rotor_right.backward(c6)
        #Plugboard
        c7 = self.plugboard.get_plugboard_output(c7)
        return c7

    def encrypt(self,in_str):
        '''
            Encrypts input string
            Input: String
            Output: String
        '''
        in_num_list = [self.plugboard.get_plugboard_output(i) for i in self.to_num_list(self.only_alpha(in_str))]
        out_num_list = []
        for i in in_num_list:
            out_num_list.append(self.encrypt_int(i))
        return self.from_num_list(out_num_list)

    def set_plugboard(self,plugboard_connections):
        '''
            Sets connections of the plugboard
        '''
        for i in plugboard_connections:
            self.plugboard.set_connection(ord(i[0])-65,ord(i[1])-65)
