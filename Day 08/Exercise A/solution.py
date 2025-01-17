t_orig, t_proc, orig, proc = 0, 0, [], []

with open("code.txt") as code:
    for line in code:
        orig.append(line.strip())

for l in orig:
    t_orig += len(l)
    
    i, q, b, x, temp = 0, 0, 0, 0, l
    
    while i < len(temp) - 1:
        if temp[i] == "\\" and temp[i + 1] == "\"":
            q += 1
            
            temp = temp[:i] + ".." + temp[i + 2:]
        if temp[i] == "\\" and temp[i + 1] == "\\":
            b += 1
            
            temp = temp[:i] + ".." + temp[i + 2:]
        if temp[i] == "\\" and temp[i + 1] == "x":
            x += 1
            
            temp = temp[:i] + "...." + temp[i + 4:]
        
        i += 1
    
    t_proc += len(l) - (2 + q + b + 3 * x)

print(t_orig - t_proc)