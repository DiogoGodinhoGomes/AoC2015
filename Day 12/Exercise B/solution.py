text, uniq = [], set()

with open("code.txt") as file:
    for line in file:
        text = line.strip()

for i in [c for c in text]:
    if (ord(i) < ord("0") or ord(i) > ord("9")) and ord(i) != ord("-"):
        uniq.add(i)

text = text.replace(":\"red\"", "X")

for i in uniq:
    if i != "{" and i != "}" and i != "[" and i != "]":
        text = text.replace(i, " ")

while "  " in text:
    text = text.replace("  ", " ")

while "X" in text:
    mxm, clvl = 0, 0
    
    for i, e in enumerate(text):
        if e == "{":
            clvl += 1
        elif e == "}":
            clvl -= 1
        
        assert clvl >= 0
        
        mxm = max(mxm, clvl)
    
    x, clvl, torm, tokp = False, 0, [], []
    
    for i, e in enumerate(text):
        if e == "{":
            clvl += 1
            
            if clvl == mxm:
                torm.append(i)
                
                tokp.append(i)
        elif e == "}":
            clvl -= 1
            
            if clvl == mxm - 1:
                if x:
                    torm.append(i)
                    
                    tokp.pop(-1)
                else:
                    torm.pop(-1)
                    
                    tokp.append(i)
                
                x = False
        elif e == "X":
            if clvl == mxm:
                x = True
        
        assert clvl >= 0
    
    assert len(torm) % 2 == 0 and len(tokp) % 2 == 0 and clvl == 0
    
    i = 0
    
    while i < len(torm):
        l = torm[i + 1] - torm[i] + 1
        
        text = text[:torm[i]] + (" " * l) + text[torm[i + 1] + 1:]
        
        i += 2
    
    i = 0
    
    while i < len(tokp):
        l = tokp[i + 1] - tokp[i] + 1
        
        temp = text[tokp[i] + 1:tokp[i + 1]].replace("["," ").replace("]"," ").strip()
        
        while "  " in temp:
            temp = temp.replace("  ", " ")
        
        ttl = sum([int(c) for c in temp.strip().split()])
        
        nl = len(str(ttl))
        
        text = text[:tokp[i]] + (" " * (l - nl - 1)) + str(ttl) + " " + text[tokp[i + 1] + 1:]
        
        i += 2

text = text.replace("X", "").replace("{"," ").replace("}"," ").replace("["," ").replace("]"," ").strip()

while "  " in text:
    text = text.replace("  ", " ")

print(sum([int(c) for c in text.strip().split()]))