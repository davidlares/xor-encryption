#!/usr/bin/python

import string
import random

# this will generate a random key used for the XOR encrpytion for 1kb = same as the TCP socket size
key = ''.join(random.choice(string.ascii_lowercase + string.ascii_uppercase + string.digits + '^!\$%&/()=?{[]}+~#-_.:,;<>|\\') for _ in range(1024))
# printing data
print(key)
print('\n' + 'Key length' + str(len(key)))

# XOR encryption should be gt the length of the message
message = 'ipconfig'
print("Hardcoded message is: " + message + "\n")

def str_xor(message, key):
    # split the message abd the XOR key in a tuple format
    # each tuple is converted in to an integer value (ord)
    # then performs exclusive XOR on them
    # merge the result on ASCII
    # finally join them
    return "".join([chr(ord(c1) ^ ord(c2)) for (c1,c2) in zip(message,key)])

# implemented methods with the same key
encryption = str_xor(message, key)
print('Encrypted message: ' + encryption + "\n")

decryption = str_xor(encryption, key)
print('Decrypted message: ' + decryption + "\n")
