table, points, period = [], 0, 2503

with open("code.txt") as file:
    for line in file:
        temp = line.strip().split()
        
        table.append([(temp[0], int(temp[3]), int(temp[6]), int(temp[-2])), 1, int(temp[6]), 0, 0])

for i in range(period):
    mxm = 0
    
    for e in table:
        if e[1] > 0:
            e[3] += e[0][1]
        
        if e[2] > 1:
            e[2] -= 1
        else:
            e[1] *= -1
            
            if e[1] > 0:
                e[2] = e[0][2]
            else:
                e[2] = e[0][3]
    
    for e in table:
        mxm = max(mxm, e[3])
    
    for e in table:
        if e[3] == mxm:
            e[4] += 1

for e in table:
    points = max(points, e[4])

print(points)