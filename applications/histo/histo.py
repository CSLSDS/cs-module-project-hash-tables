# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.
from os.path import dirname, join, realpath
import sys

given_freq = ['E', 'T', 'A', 'O', 'H', 'N', 'R', 'I', 'S', 'D', 'L', 'W', 'U',
'G', 'F', 'B', 'M', 'Y', 'C', 'P', 'K', 'V', 'Q', 'J', 'X', 'Z']

f = join(dirname(realpath(__file__)), 'robin.txt')

with open(f) as f:
    robin=(f.read())

def histo(s):
    s = s.lower().split()
    freq = {}
    for w in s:
        if w not in freq:
            freq[w] = 1
        else:
            freq[w] += 1
    sort = dict([(key, value) for (key, value) in sorted(freq.items())])
    ordered = dict(sorted(sort.items(), key=lambda e: e[1], reverse=True))
    for key, value in ordered.items():
        tally = '#' * value
        print(f'{tally} {key}')

print(histo(robin))