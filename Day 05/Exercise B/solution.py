strs, total = [], 0

with open("code.txt") as code:
    for line in code:
        strs.append(line.strip())

for e in strs:
    i, j, repeat, middle = 0, 0, False, False
    
    while i < len(e) - 2 and not middle:
        if e[i] == e[i + 2]:
            middle = True
        
        i += 1
    
    while j < len(e) - 1 and not repeat:
        if e[j:j+2] in e[0:j] or e[j:j+2] in e[j + 2:]:
            repeat = True
        
        j += 1
    
    if middle and repeat:
        total += 1

print(total)