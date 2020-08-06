# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.
from os.path import dirname, join, realpath
import sys

given_freq = ['E', 'T', 'A', 'O', 'H', 'N', 'R', 'I', 'S', 'D', 'L', 'W', 'U',
'G', 'F', 'B', 'M', 'Y', 'C', 'P', 'K', 'V', 'Q', 'J', 'X', 'Z']

ciphertext = join(dirname(realpath(__file__)), 'ciphertext.txt')

with open(ciphertext) as f:
    ciphertext=(f.read())

# given these, must first establish freq char map for ciphertext
#   utilizing two functions from lecture

def char_freq(s):
    freq = {}
    for c in s:
        if c not in given_freq:
            continue
        if c not in freq:
            freq[c] = 1
        else:
            freq[c] += 1

    return sorted(list(freq.items()), key=lambda e: e[1], reverse=True)

def blindcaesar(s):
    ''' 1. take in text,
        2. do freq analysis,
        3. map to given_freq
        4. return decoded s '''

    cfreq = char_freq(s)
    decoder = {cfreq[i][0]:given_freq[i] for i in range(len(given_freq))}
    decoded = []
    for c in s:
        if c in decoder:
            decoded.append(decoder[c])
        else:
            decoded.append(c)

    return ''.join(decoded)

print(blindcaesar(ciphertext))



# decodeTable = {value:key for (key,value) in encodeTable.items()}
