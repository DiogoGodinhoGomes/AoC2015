import numpy as np
import itertools as it

table, names, mxm, clr, hgt = [], [], 100, 500, 0

with open("code.txt") as file:
    for line in file:
        temp = line.replace(":","").replace(",","").strip().split()
        
        names.append(temp[0])
        
        i, cln = 2, []
        
        while i < len(temp):
            cln.append(int(temp[i]))
            
            i += 2
        
        table.append(cln)

tmp, fnl, table, pos = [], [], np.array(table), np.array(list(it.product(range(mxm + 1), repeat = len(names) - 1)))

for e in pos:
    if sum(e) <= mxm:
        tmp.append(list(e) + [mxm - sum(e)])

tmp = np.array(tmp)

for e in tmp:
    if sum(e * table[:,4]) == 500:
        fnl.append(e)

fnl = np.array(fnl)

for e in fnl:
    ttl = 1
    
    for i in range(len(table[0]) - 1):
        ttl *= max(0, sum(e * table[:,i]))
    
    hgt = max(hgt, ttl)

print(hgt)