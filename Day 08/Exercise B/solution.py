t_orig, t_proc, orig = 0, 0, []

with open("code.txt") as code:
    for line in code:
        orig.append(line.strip())

for l in orig:
    t_orig += len(l)
    
    q, b = 0, 0
    
    for i in l:
        if i == "\"":
            q += 1
        if i == "\\":
            b += 1
    
    t_proc += len(l) + (2 + q + b)

print(t_proc - t_orig)