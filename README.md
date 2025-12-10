# Enigma Machine
This project contains an enigma simulator, as well as a decryptor.

## Requirements
```
1. python 3.9.x
2. pip3
3. Python Modules:
    a. Flask
    b. flask-cors
    c. sys
    d. os
```
## Installation
In case you don't have a python installation, you can install it using:
1. Linux:
  ```
  sudo apt-get install python3 python3-pip
  ```
2. Windows:
Head over to https://www.python.org/downloads/windows/ and follow the instructions there.

The ```os``` and ```sys``` modules come along with your python installation, but you'll have to install ```Flask```. This can be done using:
```
pip install flask flask-cors
or
pip3 install flask flask-cors
```

Get this project by git cloning this repository using
```
git clone https://github.com/gall1frey/enigma_decoder
```

## Usage
### GUI
The project comes with a GUI. This is purely for conceptual purposes, to show how an enigma machine would work. It doesn't allow for a lot of tweaking.

To launch the GUI, open a terminal inside the ```gui``` directory and run the ```enigma_run.py``` python file using
```
python3 enigma_run.py
```
Then open a browser, ideally on a laptop/desktop, and head to http://localhost:5000

In the browser, once you've set the rotors(buttons on the bottom right) and their configurations, you can begin typing letters on your keyboard.

You should be able to see encrypted letters light up on the screen.

### The Enigma Class
The enigma machine class in this project is a simulator of an actual enigma machine, where you can do almost everything that can be done on an actual enigma machine.

The class allows you to set the reflector, rotors, their positions and even the ring positions and plugboard(This couldn't be done in the GUI).

To use the enigma class, start with importing the class into your script, and creating an object of the class.
```python
from enigma import Enigma

e = Enigma(rotors='I II IV',
           reflector='B',
           rotor_positions=[3,4,10],
           ring_settings=[2,4,0],
           plugboard_connections=[('A','F'),('G','T')])
```
Then, encryption can be done by the ```encrypt()``` method. This method takes plaintext as argument and returns the encrypted string.
```python
encrypted_text = e.encrypt('Plain Text')
```
*If the reflector, rotors, rotor positions, ring settings and plugboard connections are known, passing the ciphertext to the encrypt function will return the plaintext.*

### Enigma Decoder
This is an enigma decoder that performs a statistically optimized bruteforce attack on the ciphertext.

Check out computerphile's video for explanation of the attack: https://www.youtube.com/watch?v=RzWB5jL5RX0

This script is based on the attack performed in that video, so thanks Computerphile!

#### Running the attack:
First import all functions from the ```decoder.py``` script.
We'll only be using the decrypt function, but the others need to be imported because the decrypt function depends on them.
```python
from decoder import *
```
Then, we decrypt:
```python
pt, key = decrypt(ciphertext,available_rotors,plugboard_connections,max_keys,IOC)
```
This function returns the decrypted plaintext as well as the key.
The key is a class that includes all the components that constitute an enigma key: rotors, rotor positions, ring settings, plugboard connections and the reflector.
