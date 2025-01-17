import numpy as np
import itertools as it

ctnrs, fnl, dtnr, total = [], [], {}, 150

with open("code.txt") as file:
    for line in file:
        ctnrs.append(int(line.strip()))

ctnrs = np.array(sorted(ctnrs))

pos = list(it.product(range(2), repeat = len(ctnrs)))

for e in pos:
    if sum(ctnrs * np.array(list(e))) == total:
        fnl.append(e)
        
        if sum(e) not in dtnr.keys():
            dtnr[sum(e)] = 0
        
        dtnr[sum(e)] += 1

mnm = len(ctnrs)

for k in dtnr.keys():
    mnm = min(mnm, k)

print(dtnr[mnm])