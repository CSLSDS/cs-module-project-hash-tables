import os
import random

pwd = os.path.dirname(os.path.realpath(__file__))

# Read in all the words in one go
with open(os.path.join(pwd, "input.txt")) as f:
    words = f.read().split()

options = {}
beginword = []
endword = []
initpunc = 'ABCDEFGHIJKLMNOPQRSTUVWZYZ'
termpunc = '."?"!"'

# Analyze which words can follow other words
for i in range(len(words)-1):
    word = words[i]
    next = words[i + 1]
    if word not in options:
        # initialize list of nextwords for word, stored in options
        options[word] = [next]
    else: # else append
        options[word].append(next)
    
    if word[0] in initpunc:
        beginword.append(word)
    if word[-2:] in termpunc:
        endword.append(word)
    if len(word) > 1:
        if word[1] in initpunc:
            beginword.append(word)

# Construct 5 random sentences
for sentence in range(5):
    toprint = [random.choice(beginword)]
    while toprint[-1] not in endword and toprint[-1] in options:
        toprint.append(random.choice(options[toprint[-1]]))
    print(' '.join(toprint))

