'''

'''
from flask import Flask, render_template, request
import sys
import os
sys.path.append(os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'enigma_machine')))
from enigma import Enigma

app = Flask(__name__)
app.config["DEBUG"] = True

enigma = Enigma()
enigma_settings = {
    'rotor_l': None,
    'rotor_m': None,
    'rotor_r': None,
    'rotor_pos': None,
    'ring_pos': [0,0,0],
    'reflector': None,
    'plugboard': []
}

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/encrypt', methods=['POST'])
def enc():
    global enigma
    print(request.form['data'])
    if None in enigma_settings.values() or '' in enigma_settings.values():
        return 'Check your settings first!'
    return enigma.encrypt(request.form['data'])

@app.route('/settings', methods=['POST'])
def settings():
    global enigma
    enigma_settings['rotor_l'] = request.form['rotor_l']
    enigma_settings['rotor_m'] = request.form['rotor_m']
    enigma_settings['rotor_r'] = request.form['rotor_r']
    enigma_settings['reflector'] = request.form['reflector']
    enigma_settings['rotor_pos'] = eval(request.form['rotor_pos'])
    enigma_settings['rotor_pos'] = [int(i) for i in enigma_settings['rotor_pos']]
    print(enigma_settings)
    if not (None in enigma_settings.values() or '' in enigma_settings.values()):
        rotors = enigma_settings['rotor_l'] + ' ' + enigma_settings['rotor_m'] + ' ' + enigma_settings['rotor_r']
        enigma = Enigma(rotors,enigma_settings['reflector'],enigma_settings['rotor_pos'])
        print("ENIGMA SET!")
    return 'GOOD'

app.run()
