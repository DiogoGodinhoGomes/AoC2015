total, flag, inst, dtnr = 0, True, [], {}

with open("code.txt") as code:
    for line in code:
        temp = line.split()
        
        for i, e in enumerate(temp):
            try:
                temp[i] = int(e)
            except:
                pass
        
        inst.append([1] + temp)

while flag:
    flag = False
    
    for l in inst:
        if l[0] == 1:
            if l[1] == "NOT" and (type(l[2]) == int or l[2] in dtnr):
                if l[2] in dtnr:
                    a = dtnr[l[2]]
                elif type(l[2]) == int:
                    a = l[2]
                else:
                    assert()
                
                dtnr[l[-1]] = ~a % pow(2, 16)
                
                flag, l[0] = True, 0
            elif l[2] in ["AND", "OR", "LSHIFT", "RSHIFT"]:
                if type(l[1]) == int or l[1] in dtnr:
                    if l[1] in dtnr:
                        a = dtnr[l[1]]
                    elif type(l[1]) == int:
                        a = l[1]
                    else:
                        assert()
                    
                    if type(l[3]) == int or l[3] in dtnr:
                        if l[3] in dtnr:
                            b = dtnr[l[3]]
                        elif type(l[3]) == int:
                            b = l[3]
                        else:
                            assert()
                        
                        if l[2] == "AND":
                            dtnr[l[-1]] = (a & b) % pow(2, 16)
                        elif l[2] == "OR":
                            dtnr[l[-1]] = (a | b) % pow(2, 16)
                        elif l[2] == "LSHIFT":
                            dtnr[l[-1]] = (a << b) % pow(2, 16)
                        elif l[2] == "RSHIFT":
                            dtnr[l[-1]] = (a >> b) % pow(2, 16)
                        else:
                            assert()
                        
                        flag, l[0] = True, 0
            elif type(l[1]) is int or l[1] in dtnr:
                if l[1] in dtnr:
                    a = dtnr[l[1]]
                elif type(l[1]) == int:
                    a = l[1]
                else:
                    assert()
                
                dtnr[l[-1]] = a % pow(2, 16)
                
                flag, l[0] = True, 0

for l in inst:
    if l[0] == 0:
        total += 1

assert(total == len(inst))

print(dtnr["a"])