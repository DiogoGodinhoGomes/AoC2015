import numpy as np

dim, total, inst = 1000, 0, []

with open("code.txt") as code:
    for line in code:
        temp = 5
        
        if "on" in line:
            temp = 1
        elif "off" in line:
            temp = -1
        elif "toggle" in line:
            temp = 0
        else:
            assert()
        
        n = [int(s) for s in line.replace(",", " ").split() if s.isdigit()]
        
        inst.append([temp] + n)

array = np.ones((dim, dim)) * (-1)

for e in inst:
    assert(len(e) == 5)
    
    for i in range(e[1], e[3] + 1):
        for j in range(e[2], e[4] + 1):
            if e[0] * e[0] == 1:
                array[i][j] = e[0]
            elif e[0] == 0:
                array[i][j] *= -1
            else:
                assert()

for i in range(len(array)):
    for j in range(len(array[i])):
        if array[i][j] > 0:
            total += 1

print(total)