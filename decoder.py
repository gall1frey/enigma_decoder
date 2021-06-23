from metrics.metric import IOC
from keys.keys import enigmaKey
import sys
import os
sys.path.append(os.path.abspath('./enigma_machine'))
from enigma import Enigma

def floor_mod(a,b):
    '''
        Helper function to calculate floor mod
        Input: two integers, a and bug
        Output: floor mod of a and b
    '''
    return a - ((a//b) * b)

def find_rotor_configurations(ciphertext,available_rotors,plugboard,required_keys,fitness_func):
    '''
        Function to find possible rotor configurations
        Input:
                ciphertext: string
                available_rotors: int (3,5,8)
                plugboard: tuple list
                required_keys: int
                fitness_func: func object
    '''
    best_keys = []
    if available_rotors == 3:   rotors_list = ['I','II','III']
    elif available_rotors == 3:   rotors_list = ['I','II','III','IV','V']
    else:   rotors_list = ['I','II','III''IV','V','VI','VII','VIII']
    for rotor1 in rotors_list:
        for rotor2 in rotors_list:
            for rotor3 in rotors_list:
                if rotor1 == rotor3 or rotor2 == rotor3 or rotor1 == rotor2:
                    continue
                print("TRYING:",rotor1+' '+rotor2+' '+rotor3)
                max_fitness = 0.0
                for i in range(26):
                    for j in range(26):
                        for k in range(26):
                            e = Enigma(rotor1+' '+rotor2+' '+rotor3,'B',[i,j,k],[0,0,0],plugboard)
                            decrypted = e.encrypt(ciphertext)
                            fitness = fitness_func(decrypted)
                            if fitness > max_fitness:
                                max_fitness = fitness
                                optimal_rotors = rotor1+' '+rotor2+' '+rotor3
                                optimal_pos = [i,j,k]
                                new_best = enigmaKey(optimal_rotors,optimal_pos,'B',[0,0,0],plugboard,fitness)
                best_keys.append(new_best)
    best_keys.sort(key=lambda x: x.score,reverse=True)
    return best_keys[:required_keys]

def find_ring_configuration(ciphertext,key,rotor,fitness_func):
    '''
        Function to find possible ring configuration of a rotor
        Input:
                ciphertext: string
                key: enigmaKey object
                rotor: int (index of rotor: 0/1/2)
                fitness_func: func object
    '''
    rotors = key.rotors
    original_pos = key.pos
    original_ring = key.ring_settings or [0,0,0]
    plugboard = key.plugboard
    optimal_ring_setting = 0; max_fitness = 0.0
    for i in range(0,26):
        cur_pos = original_pos.copy()
        cur_ring = original_ring.copy()
        cur_pos[rotor] = floor_mod(cur_pos[rotor] + i, 26);
        cur_ring[rotor] = i
        e = Enigma(rotors,key.reflector,cur_pos,cur_ring,plugboard)
        decrypted = e.encrypt(ciphertext)
        fitness = fitness_func(decrypted)
        if fitness > max_fitness:
            max_fitness = fitness
            optimal_ring_setting = i
    return optimal_ring_setting

def find_ring_configurations(ciphertext,key,fitness_func):
    '''
        Function to find possible ring configurations
        Input:
                ciphertext: string
                key: enigmaKey object
                fitness_func: func object
    '''
    new_key = enigmaKey(key.rotors,key.pos,key.reflector,key.ring_settings,key.plugboard,0)
    #first optimize right rotor, then middle
    print("Working on right rotor...")
    optimal_right_index = find_ring_configuration(ciphertext,key,2,fitness_func)
    new_key.ring_settings[2] = optimal_right_index
    new_key.pos[2] = (new_key.pos[2] + optimal_right_index) % 26
    print("Working on middle rotor...")
    optimal_middle_index = find_ring_configuration(ciphertext,key,1,fitness_func)
    new_key.ring_settings[1] = optimal_middle_index
    new_key.pos[1] = (new_key.pos[1] + optimal_middle_index) % 26
    e = Enigma(new_key.rotors,new_key.reflector,new_key.pos,new_key.ring_settings,new_key.plugboard)
    decrypted = e.encrypt(ciphertext)
    new_key.score = fitness_func(decrypted)
    return new_key

def decrypt(ciphertext,available_rotors,plugboard,required_keys,fitness_func):
    best_rotor_configurations = find_rotor_configurations(ciphertext,available_rotors,plugboard,required_keys,fitness_func)
    print("Top {} rotor configurations:".format(required_keys))
    for i in best_rotor_configurations:
        print(i.rotors, i.score)
    dec_key = find_ring_configurations(ciphertext,best_rotor_configurations[0],IOC)
    e = Enigma(dec_key.rotors,dec_key.reflector,dec_key.pos,dec_key.ring_settings,dec_key.plugboard)
    decrypted = e.encrypt(ciphertext)
    return decrypted,dec_key

if __name__ == '__main__':
    ct = 'MQKPMKOEPJBIGRJZKNXXGIELJQRXMJIXDWYINNHXKEFDZXJFEQSMSMPAFCDAYVSPHEJSRZKNHBZNSXFHHKHERMIXQTUKWQDOHIVSDZWYIRYONCTMTPAKMHBIYONBRPHFPABSCKOAULPRUOMSIBNSHJKVTFAVLDDKCYIUNJGEZPFDYTOAFILUPSBMKFTGDDZVOKYKKDQDRHZGBZWBQABTYHWJQWVIAOQEHLBQSUIWNCUDWPEZFZVVJWUKRQLWXADKYEHHMGRUFAAGPYCONELNMIBVGCSKNRRDOCOWDUUPTROQKHJEOLDXQHQIYSWLMEJLTKQMFAYVYZSJAAYFJADQQJMSFODVBDJYNPIEMMZTTVACKAORJKZSQYIHETRYJCRYESUXHPXEXMPWVOYJNBEDKXRGHCLZFMNYYRREPVJFHPKSAAIGBBRABZDZXYKSCZNKAGHXNSMQJCPCVHTUIZFVZMJTQOHDZCLFLAPDKCIJMZLKRMCCHEWTYMZABCYBERZJBVCEYUQYGSHWHIMTVB'
    pt, key = decrypt(ct,3,[],3,IOC)
    print("DECRYPTED TEXT:")
    print(decrypted)
    print("The above text was decrypted with an IOC score of",key.score)
    print("ROTORS:",key.rotors)
    print("ROTOR CONFIG:",key.pos,key.ring_settings)
    print("PLUGBOARD:",key.plugboard)
