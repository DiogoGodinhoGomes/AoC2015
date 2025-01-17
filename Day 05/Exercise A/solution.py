strs, total = [], 0

with open("code.txt") as code:
    for line in code:
        strs.append(line.strip())

for e in strs:
    vowels, double, allowed, prev = 0, False, True, ""
    
    for i, c in enumerate(e):
        if c == "a" or c == "e" or c == "i" or c == "o" or c == "u":
            vowels += 1
        
        if i > 0 and c == prev and not double:
            double = True
        
        prev = c
    
    if "ab" in e or "cd" in e or "pq" in e or "xy" in e:
        allowed = False
    
    if vowels >= 3 and double and allowed:
        total += 1

print(total)