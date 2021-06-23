'''
Author: Gallifrey (github.com/gall1frey)
Class Plugboard for Enigma
'''

class Plugboard:
    '''
        Class for plugboard of an Enigma Machine
    '''
    def __init__(self):
        '''
            Constructor of the Plugboard class
            Sets the default connections to themselves
            (A->A, B->B, C->C, etc.)
        '''
        self.setting = dict((a,a) for a in range(26))

    def set_connection(self,frm,to):
        '''
            Adds a new connection on the plugboard
            Input: From and To [Integers]
            If a connection already exists, that connection is first removed.
        '''
        if self.setting[frm] != frm:
            self.remove_connection(frm)
        if self.setting[to] != to:
            self.remove_connection(to)
        self.setting[frm] = to
        self.setting[to] = frm

    def remove_connection(self,frm):
        '''
            Removes a connection from the plugboard
            Input: From [Integer]
        '''
        to = self.setting[frm]
        self.setting[frm] = frm
        self.setting[to] = to

    def get_plugboard_output(self,in_char):
        '''
            Gets the output from the plugboard
            Input: Integer
            Output: Integer
        '''
        return self.setting[in_char]

    def get_plugboard_dict(self):
        '''
            Returns a dict of all plugboard connections
        '''
        return self.setting
