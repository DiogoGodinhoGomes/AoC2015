import itertools as it

table, people, ttls = [], set(), {}

with open("code.txt") as file:
    for line in file:
        temp = line.replace(".", "").replace("gain ", "+").replace("lose ", "-").strip().split()
        
        temp = sorted([temp[0], temp[-1], temp[2]])
        
        for e in temp[1:]:
            people.add(e)
        
        table.append(temp[1:] + [int(temp[0])])

people = sorted(list(people))

for row in table:
    temp = [people.index(row[0]), people.index(row[1])]
    
    temp = (min(temp), max(temp))
    
    if temp not in ttls.keys():
        ttls[temp] = 0
    
    ttls[temp] += row[2]

i, pos = 0, list(it.permutations(range(len(people))))

while i < len(pos):
    pos[i] = list(pos[i]) + [pos[i][0]]
    
    i += 1

i, mxm = 0, 0

while i < len(pos):
    n, total = 0, 0
    
    for n in pos[i][:-1]:
        total += ttls[(min(pos[i][n], pos[i][n + 1]), max(pos[i][n], pos[i][n + 1]))]
    
    pos[i], mxm = [total, pos[i]], max(mxm, total)
    
    i += 1

print(mxm)