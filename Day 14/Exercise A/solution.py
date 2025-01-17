table, totals, period = [], [], 2503

with open("code.txt") as file:
    for line in file:
        temp = line.strip().split()
        
        table.append([temp[0], int(temp[3]), int(temp[6]), int(temp[-2])])

for e in table:
    cycles, rest = int(period / (e[2] + e[3])), period % (e[2] + e[3])
    
    totals.append(e[1] * (cycles * e[2] + min(e[2], rest)))

print(max(totals))