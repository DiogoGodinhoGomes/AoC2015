import numpy as np
import itertools as it

l, forb = ord("z") - ord("a") + 1, np.array([ord("i"), ord("l"), ord("o")]) - ord("a")

with open("code.txt") as file:
    for line in file:
        orig = np.array([ord(c) - ord("a") for c in line.strip()])

i, sequence, pairs, forbidden = 0, False, False, False

while i < len(orig) and not forbidden:
    if orig[i] in forb:
        j, forbidden = i + 1, True
        
        while j < len(orig):
            orig[j] = l - 1
            
            j += 1
    
    i += 1

forbidden = False

while not sequence or not pairs or forbidden:
    orig[-1] += 1
    
    if orig[-1] in forb:
        orig[-1] += 1
    
    for i in range(len(orig))[:0:-1]:
        if orig[i] == l:
            orig[i] = 0
            
            orig[i - 1] += 1
            
            if orig[i - 1] in forb:
                orig[i - 1] += 1
    
    orig[0] = orig[0] % l
    
    i, forbidden = 0, False
    
    while i < len(orig) and not forbidden:
        if orig[i] in forb:
            forbidden = True
        
        i += 1
    
    diff = orig[1:] - orig[:-1]
    
    i, sequence = 0, False
    
    while i < len(diff) - 1 and not sequence:
        if diff[i] == 1 and diff[i + 1] == 1:
            sequence = True
        
        i += 1
    
    zeros = []
    
    for i, elem in enumerate(diff):
        if elem == 0:
            zeros.append(i)
    
    pos, final = list(it.combinations(zeros, 2)), []
    
    for elem in pos:
        if abs(elem[0] - elem[1]) > 1:
            final.append(elem)
    
    i, pairs = 0, False
    
    while i < len(final) and not pairs:
        if orig[final[i][0]] != orig[final[i][1]]:
            pairs = True
        
        i += 1
    
    i, string = 0, ""

    while i < len(orig):
        string += chr(orig[i] + ord("a"))
        
        i += 1

    print(string)

i, string = 0, ""

while i < len(orig):
    string += chr(orig[i] + ord("a"))
    
    i += 1

print(string)