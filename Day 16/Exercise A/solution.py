key, sues, fnl = {}, [], []

# 102 is too low!

with open("excode.txt") as file:
    for line in file:
        temp = line.replace(":", "").strip().split()
        
        if temp[0] not in key.keys():
            key[temp[0]] = 0
        
        key[temp[0]] += int(temp[1])

with open("code.txt") as file:
    for line in file:
        i, dtnr, temp = 2, {}, line.replace(":", "").replace(",", "").strip().split()
        
        while i < len(temp):
            if temp[i] not in dtnr.keys():
                dtnr[temp[i]] = 0
            
            dtnr[temp[i]] += int(temp[i + 1])
            
            i += 2
        
        sues.append(dtnr)

for i, sue in enumerate(sues):
    match = True
    
    for k in sue.keys():
        if key[k] != sue[k]:
            match = False
            
            break
    
    if match:
        fnl.append(i + 1)

assert len(fnl) == 1

print(fnl[0])