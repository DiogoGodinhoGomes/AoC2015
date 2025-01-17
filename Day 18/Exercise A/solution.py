import copy as cp

ogrid, total, steps = [], 0, 100

dirs = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]

with open("code.txt") as file:
    for line in file:
        ogrid.append([c for c in line.strip()])

ngrid = cp.deepcopy(ogrid)

for i in range(steps):    
    for r in range(len(ogrid)):
        for c in range(len(ogrid[r])):
            ons = 0
            
            for d in dirs:
                nr, nc = r + d[0], c + d[1]
                
                if nr >= 0 and nc >= 0 and nr < len(ogrid) and nc < len(ogrid[nr]):
                    if ogrid[nr][nc] == "#":
                        ons += 1
            
            if ogrid[r][c] == "#" and ons not in [2, 3]:
                ngrid[r][c] = "."
            
            if ogrid[r][c] == "." and ons == 3:
                ngrid[r][c] = "#"
    
    ogrid = cp.deepcopy(ngrid)

for r in ogrid:
    for c in r:
        if c == "#":
            total += 1

print(total)